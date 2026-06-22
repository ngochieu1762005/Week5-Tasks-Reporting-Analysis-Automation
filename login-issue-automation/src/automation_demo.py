import logging
from pathlib import Path
from models import Ticket
from hr_client import HRClient
from lms_client import LMSClient
from login_automation_service import LoginAutomationService

Path("logs").mkdir(exist_ok=True)
logging.basicConfig(filename="logs/automation.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

TEST_TICKETS = [
    Ticket("00001", "LMS Login Issue - Teacher cannot access account", "Teacher cannot login to LMS. Account seems disabled.", "teacher01@example.com"),
    Ticket("00007", "LMS Login Issue - Old employee cannot access account", "User cannot login to LMS.", "old.employee@example.com"),
    Ticket("00008", "LMS Login Issue - Unknown user", "User cannot access LMS account.", "unknown.person@example.com"),
    Ticket("00009", "LMS Performance Issue", "The system is slow for class WEB101.", "teacher01@example.com"),
    Ticket("00010", "Cannot login to LMS", "I cannot login to my account.", None),
    Ticket("00011", "LMS account may be hacked", "I think my LMS account was hacked.", "teacher01@example.com"),
]

if __name__ == "__main__":
    service = LoginAutomationService(HRClient(), LMSClient(), dry_run=True)
    print("===== Week 5 Login Issue Automation Demo =====")
    for ticket in TEST_TICKETS:
        print(f"\nProcessing ticket {ticket.ticket_id} - {ticket.title}")
        result = service.process(ticket)
        print("Result:", result)
