import os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv
from models import Ticket
from hr_client import HRClient
from lms_client import LMSClient
from login_automation_service import LoginAutomationService

load_dotenv("config/.env")
SECRET = os.getenv("WEBHOOK_SECRET", "change-this-secret")
HOST = os.getenv("WEBHOOK_HOST", "0.0.0.0")
PORT = int(os.getenv("WEBHOOK_PORT", "8080"))

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/webhook/odoo-ticket":
            self.send_response(404); self.end_headers(); return

        token = self.headers.get("X-Webhook-Secret")
        if token != SECRET:
            self.send_response(401); self.end_headers(); self.wfile.write(b"Unauthorized"); return

        length = int(self.headers.get("Content-Length", 0))
        payload = json.loads(self.rfile.read(length).decode("utf-8"))

        ticket = Ticket(
            ticket_id=str(payload.get("ticket_id") or payload.get("id")),
            title=payload.get("title") or payload.get("name") or "",
            description=payload.get("description") or "",
            requester_email=payload.get("requester_email") or payload.get("partner_email"),
            requester_name=payload.get("requester_name") or payload.get("partner_name"),
            priority=payload.get("priority"),
            stage=payload.get("stage"),
            tags=payload.get("tags") or [],
        )
        service = LoginAutomationService(HRClient(), LMSClient(), dry_run=True)
        result = service.process(ticket)

        body = json.dumps(result.__dict__, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    print(f"Webhook server running on http://{HOST}:{PORT}/webhook/odoo-ticket")
    HTTPServer((HOST, PORT), Handler).serve_forever()
