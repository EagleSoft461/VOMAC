from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict

@dataclass(frozen=True)
class Event:
    type: str
    source: str
    payload: Dict[str, Any]

    timestamp: datetime = field(default_factory=datetime.utcnow)