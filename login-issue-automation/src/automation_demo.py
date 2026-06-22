import logging
from pathlib import Path
from models import Ticket
from hr_client import HRClient
from lms_client import LMSClient
from login_automation_service import LoginAutomationService

Path("logs").mkdir(exist_ok=True)
logging.basicConfig(filename="logs/automation.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

TEST_TICKETS = [
    Ticket("00001", "LMS Login Issue - Teacher cannot access account", "Teacher cannot login to LMS. Account seems disabled.", "teacher01@mindx.com"),
    Ticket("00007", "LMS Login Issue - Terminated teacher cannot access account", "User cannot login to LMS.", "terminated.teacher@mindx.com"),
    Ticket("00008", "LMS Login Issue - Unknown user", "User cannot access LMS account.", "unknown.user@mindx.com"),
    Ticket("00009", "LMS Performance Issue", "The system is slow for class WEB101.", "teacher02@mindx.com"),
    Ticket("00010", "Cannot login to LMS", "I cannot login to my account.", None),
    Ticket("00011", "LMS account may be hacked", "I think my LMS account was hacked.", "teacher01@mindx.com"),
    Ticket("00012", "LMS Login Issue - Locked account", "User cannot login because the account is locked.", "locked.user@mindx.com"),
    Ticket("00013", "LMS Login Issue - Suspended account", "User cannot login to LMS.", "suspended.user@mindx.com"),
    Ticket("00014", "LMS Login Issue - Contractor account", "Contractor cannot access LMS account.", "contractor01@mindx.com"),
]

if __name__ == "__main__":
    service = LoginAutomationService(HRClient(), LMSClient(), dry_run=True)
    print("===== Week 5 Login Issue Automation Demo =====")
    for ticket in TEST_TICKETS:
        print(f"\nProcessing ticket {ticket.ticket_id} - {ticket.title}")
        result = service.process(ticket)
        print("Result:", result)
