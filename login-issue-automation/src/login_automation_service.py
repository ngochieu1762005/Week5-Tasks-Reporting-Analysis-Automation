import logging
from models import Ticket, AutomationResult
from detector import is_login_issue, has_security_risk

RESOLVED_MESSAGE = """Hello,

Your LMS account has been checked and reactivated. Please try logging in again.

If the issue still occurs, please reply directly in this ticket so the support team can continue investigating.

Best regards,
Support Team"""

MANUAL_REVIEW_MESSAGE = """Hello,

We have received your LMS login support request. This ticket is being moved to manual review so the support team can verify additional information before making any account changes.

We will update you in this ticket after the review is completed.

Best regards,
Support Team"""


class LoginAutomationService:
    def __init__(self, hr_client, lms_client, odoo_client=None, dry_run=True):
        self.hr_client = hr_client
        self.lms_client = lms_client
        self.odoo_client = odoo_client
        self.dry_run = dry_run
        self.logger = logging.getLogger("login_automation")

    def _note(self, ticket_id, note):
        self.logger.info("ticket=%s note=%s", ticket_id, note)
        if self.odoo_client and not self.dry_run:
            self.odoo_client.add_internal_note(int(ticket_id), note)
        print(f"[Odoo Note] Ticket {ticket_id}: {note}")

    def _tag(self, ticket_id, tag):
        self.logger.info("ticket=%s tag=%s", ticket_id, tag)
        if self.odoo_client and not self.dry_run:
            self.odoo_client.add_tag_by_name(int(ticket_id), tag)
        print(f"[Odoo Tag] Ticket {ticket_id}: {tag}")

    def _send(self, ticket_id, email, message):
        self.logger.info("ticket=%s send_response_to=%s", ticket_id, email)
        if self.odoo_client and not self.dry_run:
            self.odoo_client.send_message_to_requester(int(ticket_id), message)
        print(f"[Response] To {email}: {message.splitlines()[0]}")

    def _stage(self, ticket_id, stage_name, stage_id=None):
        self.logger.info("ticket=%s stage=%s", ticket_id, stage_name)
        if self.odoo_client and not self.dry_run and stage_id:
            self.odoo_client.update_stage(int(ticket_id), int(stage_id))
        print(f"[Odoo Stage] Ticket {ticket_id}: {stage_name}")

    def process(self, ticket: Ticket, solved_stage_id=None, manual_review_stage_id=None) -> AutomationResult:
        self.logger.info("start ticket=%s", ticket.ticket_id)

        if not ticket.ticket_id:
            return AutomationResult(ticket_id="unknown", result="failed", reason="missing_ticket_id")

        if has_security_risk(ticket.title, ticket.description):
            self._note(ticket.ticket_id, "Manual review required: possible security or access risk detected.")
            self._tag(ticket.ticket_id, "manual-review")
            self._stage(ticket.ticket_id, "Manual Review", manual_review_stage_id)
            return AutomationResult(ticket.ticket_id, "manual_review_required", reason="security_risk")

        if not is_login_issue(ticket.title, ticket.description):
            self._note(ticket.ticket_id, "Automation skipped: ticket does not match Login Issue pattern.")
            self._tag(ticket.ticket_id, "automation-skipped")
            return AutomationResult(ticket.ticket_id, "skipped_not_login_issue", action="skip")

        self._note(ticket.ticket_id, "Automation detected pattern: Login Issue.")

        if not ticket.requester_email:
            self._note(ticket.ticket_id, "Manual review required: requester email is missing.")
            self._tag(ticket.ticket_id, "manual-review")
            self._stage(ticket.ticket_id, "Manual Review", manual_review_stage_id)
            return AutomationResult(ticket.ticket_id, "manual_review_required", reason="missing_requester_email")

        status = self.hr_client.get_employee_status(ticket.requester_email)
        self.logger.info("ticket=%s requester=%s employee_status=%s", ticket.ticket_id, ticket.requester_email, status)

        if status == "active":
            success = self.lms_client.reactivate_account(ticket.requester_email)
            if success:
                self._send(ticket.ticket_id, ticket.requester_email, RESOLVED_MESSAGE)
                self._note(ticket.ticket_id, "Automation completed: employee is active and LMS account was reactivated.")
                self._tag(ticket.ticket_id, "automation-processed")
                self._stage(ticket.ticket_id, "Solved", solved_stage_id)
                return AutomationResult(ticket.ticket_id, "resolved_by_automation", employee_status=status, action="lms_account_reactivated", message_sent=True, odoo_updated=True)
            self._note(ticket.ticket_id, "Manual review required: LMS account reactivation failed.")
            self._tag(ticket.ticket_id, "manual-review")
            self._stage(ticket.ticket_id, "Manual Review", manual_review_stage_id)
            return AutomationResult(ticket.ticket_id, "manual_review_required", reason="lms_reactivation_failed", employee_status=status)

        if status == "terminated":
            self._note(ticket.ticket_id, "Manual review required: employee status is terminated. No account reactivation performed.")
            self._send(ticket.ticket_id, ticket.requester_email, MANUAL_REVIEW_MESSAGE)
            self._tag(ticket.ticket_id, "manual-review")
            self._stage(ticket.ticket_id, "Manual Review", manual_review_stage_id)
            return AutomationResult(ticket.ticket_id, "manual_review_required", reason="terminated_employee", employee_status=status, message_sent=True)

        self._note(ticket.ticket_id, "Manual review required: employee status is unknown or cannot be verified.")
        self._tag(ticket.ticket_id, "manual-review")
        self._stage(ticket.ticket_id, "Manual Review", manual_review_stage_id)
        return AutomationResult(ticket.ticket_id, "manual_review_required", reason="unknown_employee_status", employee_status=status)
