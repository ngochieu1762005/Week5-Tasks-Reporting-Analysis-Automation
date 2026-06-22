import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from models import Ticket
from hr_client import HRClient
from lms_client import LMSClient
from odoo_api_client import OdooAPIClient
from login_automation_service import LoginAutomationService

Path("logs").mkdir(exist_ok=True)
logging.basicConfig(filename="logs/automation.log", level=os.getenv("LOG_LEVEL", "INFO"), format="%(asctime)s %(levelname)s %(message)s")

load_dotenv("config/.env")

def main():
    dry_run = os.getenv("DRY_RUN", "true").lower() == "true"
    solved_stage_id = os.getenv("ODOO_SOLVED_STAGE_ID")
    manual_review_stage_id = os.getenv("ODOO_MANUAL_REVIEW_STAGE_ID")

    odoo = OdooAPIClient.from_env()
    service = LoginAutomationService(HRClient(), LMSClient(), odoo_client=odoo, dry_run=dry_run)

    ticket_ids = odoo.search_new_tickets(limit=20)
    print(f"Found {len(ticket_ids)} tickets")

    for tid in ticket_ids:
        record = odoo.read_ticket(tid)
        data = OdooAPIClient.normalize_ticket(record)
        ticket = Ticket(**data)
        result = service.process(ticket, solved_stage_id=solved_stage_id, manual_review_stage_id=manual_review_stage_id)
        print(result)

if __name__ == "__main__":
    main()
