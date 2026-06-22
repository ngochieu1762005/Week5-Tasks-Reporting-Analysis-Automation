import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from models import Ticket
from hr_client import HRClient
from lms_client import LMSClient
from login_automation_service import LoginAutomationService

class TestLoginAutomation(unittest.TestCase):
    def setUp(self):
        self.service = LoginAutomationService(HRClient(data_path="data/hr_demo.json"), LMSClient(), dry_run=True)

    def test_active_employee_resolved(self):
        ticket = Ticket("00001", "Cannot login to LMS", "Account disabled", "teacher01@example.com")
        result = self.service.process(ticket)
        self.assertEqual(result.result, "resolved_by_automation")
        self.assertEqual(result.employee_status, "active")

    def test_terminated_employee_manual_review(self):
        ticket = Ticket("00007", "Cannot login to LMS", "Account disabled", "old.employee@example.com")
        result = self.service.process(ticket)
        self.assertEqual(result.result, "manual_review_required")
        self.assertEqual(result.reason, "terminated_employee")

    def test_unknown_employee_manual_review(self):
        ticket = Ticket("00008", "Cannot login to LMS", "Account disabled", "someone@example.com")
        result = self.service.process(ticket)
        self.assertEqual(result.result, "manual_review_required")
        self.assertEqual(result.reason, "unknown_employee_status")

    def test_non_login_skipped(self):
        ticket = Ticket("00009", "LMS Performance Issue", "System slow", "teacher01@example.com")
        result = self.service.process(ticket)
        self.assertEqual(result.result, "skipped_not_login_issue")

    def test_missing_email_manual_review(self):
        ticket = Ticket("00010", "Cannot login to LMS", "Account disabled", None)
        result = self.service.process(ticket)
        self.assertEqual(result.result, "manual_review_required")
        self.assertEqual(result.reason, "missing_requester_email")

    def test_security_risk_manual_review(self):
        ticket = Ticket("00011", "LMS account hacked", "My account was hacked", "teacher01@example.com")
        result = self.service.process(ticket)
        self.assertEqual(result.result, "manual_review_required")
        self.assertEqual(result.reason, "security_risk")

if __name__ == "__main__":
    unittest.main()
