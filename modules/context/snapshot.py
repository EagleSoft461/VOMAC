from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Set, Optional

@dataclass(frozen=True)
class ContextSnapshot:
    system_started: bool
    system_ready: bool
    system_shutdown: bool

    started_at: Optional[datetime]

    last_event_type: Optional[str]
    last_event_source: Optional[str]
    last_event_time: Optional[datetime]

    event_count: int
    event_types: Dict[str, int]

    modules_ready: Set[str]