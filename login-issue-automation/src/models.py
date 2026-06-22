from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass
class Ticket:
    ticket_id: str
    title: str
    description: str
    requester_email: Optional[str] = None
    requester_name: Optional[str] = None
    priority: Optional[str] = None
    stage: Optional[str] = None
    tags: List[str] = field(default_factory=list)

@dataclass
class AutomationResult:
    ticket_id: str
    result: str
    reason: Optional[str] = None
    employee_status: Optional[str] = None
    action: Optional[str] = None
    message_sent: bool = False
    odoo_updated: bool = False
    details: Dict[str, Any] = field(default_factory=dict)
