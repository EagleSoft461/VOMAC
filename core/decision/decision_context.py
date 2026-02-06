from dataclasses import dataclass
from typing import Any, Dict, Optional

@dataclass(frozen=True)
class DecisionContext:
    """
    Read-only input for the decision engine.

    Contains:
    - event type + payload
    - optional snapshots from context/memory modules
    """
    event_type: str
    event_payload: Dict[str, Any]

    memory_snapshot: Optional[Dict[str, Any]] = None
    context_snapshot: Optional[Dict[str, Any]] = None