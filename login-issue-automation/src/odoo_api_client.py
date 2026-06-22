import os
import ssl
import xmlrpc.client
from typing import List, Dict, Any, Optional

class OdooAPIClient:
    """
    Odoo XML-RPC API client.

    This file shows how the workflow can integrate with the real Odoo API:
    - authenticate
    - search/read ticket
    - add internal note
    - update stage
    - add tags
    - send message
    """

    def __init__(self, url: str, db: str, username: str, api_key: str, model: str = "helpdesk.ticket"):
        self.url = url.rstrip("/")
        self.db = db
        self.username = username
        self.api_key = api_key
        self.model = model
        self.uid = None
        self.common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common", context=ssl._create_unverified_context())
        self.models = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object", context=ssl._create_unverified_context())

    @classmethod
    def from_env(cls):
        return cls(
            url=os.getenv("ODOO_URL", ""),
            db=os.getenv("ODOO_DB", ""),
            username=os.getenv("ODOO_USERNAME", ""),
            api_key=os.getenv("ODOO_API_KEY", ""),
            model=os.getenv("ODOO_HELPDESK_MODEL", "helpdesk.ticket"),
        )

    def authenticate(self) -> int:
        self.uid = self.common.authenticate(self.db, self.username, self.api_key, {})
        if not self.uid:
            raise RuntimeError("Odoo authentication failed")
        return self.uid

    def _execute(self, method: str, *args, **kwargs):
        if not self.uid:
            self.authenticate()
        return self.models.execute_kw(
            self.db, self.uid, self.api_key, self.model, method, list(args), kwargs or {}
        )

    def search_new_tickets(self, limit: int = 20) -> List[int]:
        domain = [
            ["stage_id.name", "not in", ["Solved", "Closed"]],
            ["tag_ids.name", "not in", ["automation-processed", "automation-skipped", "manual-review"]],
        ]
        try:
            return self._execute("search", domain, limit=limit, order="create_date desc")
        except Exception:
            # Some Odoo instances do not support stage_id.name/tag_ids.name in a domain.
            # Use a simple fallback domain.
            return self._execute("search", [], limit=limit, order="create_date desc")

    def read_ticket(self, ticket_id: int) -> Dict[str, Any]:
        fields = ["id", "name", "description", "partner_email", "partner_name", "priority", "stage_id", "tag_ids"]
        records = self._execute("read", [ticket_id], fields=fields)
        return records[0] if records else {}

    def add_internal_note(self, ticket_id: int, note: str) -> None:
        # message_post is the standard method in mail.thread models.
        self._execute("message_post", [ticket_id], body=note, message_type="comment", subtype_xmlid="mail.mt_note")

    def send_message_to_requester(self, ticket_id: int, message: str) -> None:
        self._execute("message_post", [ticket_id], body=message, message_type="comment", subtype_xmlid="mail.mt_comment")

    def update_stage(self, ticket_id: int, stage_id: int) -> None:
        self._execute("write", [ticket_id], {"stage_id": stage_id})

    def add_tag_by_name(self, ticket_id: int, tag_name: str) -> None:
        # The tag model can vary by Odoo version. This is a common helpdesk.tag implementation.
        if not self.uid:
            self.authenticate()
        tag_model = "helpdesk.tag"
        tag_ids = self.models.execute_kw(
            self.db, self.uid, self.api_key, tag_model, "search", [[ ["name", "=", tag_name] ]], {"limit": 1}
        )
        if not tag_ids:
            tag_ids = self.models.execute_kw(
                self.db, self.uid, self.api_key, tag_model, "create", [{"name": tag_name}]
            )
            if isinstance(tag_ids, int):
                tag_ids = [tag_ids]
        self._execute("write", [ticket_id], {"tag_ids": [(4, tag_ids[0])]})

    @staticmethod
    def normalize_ticket(record: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "ticket_id": str(record.get("id")),
            "title": record.get("name") or "",
            "description": record.get("description") or "",
            "requester_email": record.get("partner_email") or None,
            "requester_name": record.get("partner_name") or None,
            "priority": record.get("priority") or None,
            "stage": record.get("stage_id", [None, None])[1] if isinstance(record.get("stage_id"), list) else None,
            "tags": record.get("tag_ids") or [],
        }
