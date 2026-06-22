import json
from pathlib import Path


class HRClient:
    """Demo HR client. Replace this class with the real HR API client in production."""

    def __init__(self, data_path: str = "data/hr_demo.json"):
        self.data_path = Path(data_path)
        if self.data_path.exists():
            self.data = json.loads(self.data_path.read_text(encoding="utf-8"))
        else:
            self.data = {}

    def get_employee_status(self, email: str) -> str:
        if not email:
            return "missing_email"
        record = self.data.get(email)
        if not record:
            return "unknown"
        return record.get("status", "unknown")
