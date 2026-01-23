from datetime import datetime
from typing import Dict, Set, Optional
from .snapshot import ContextSnapshot
from core.events.event import Event

class ContextState:
    """
    Holds the current system context.

    This object represents the *present state* of the system.
    It does not store history and does not make decisions.
    """

    def snapshot(self) -> ContextSnapshot:
        return ContextSnapshot(
        system_started=self.system_started,
        system_ready=self.system_ready,
        system_shutdown=self.system_shutdown,
        started_at=self.started_at,
        last_event_type=self.last_event_type,
        last_event_source=self.last_event_source,
        last_event_time=self.last_event_time,
        event_count=self.event_count,
        event_types=dict(self.event_types),
        modules_ready=set(self.modules_ready),
    )

    def __init__(self):
        self.system_started: bool = False
        self.system_ready: bool = False
        self.system_shutdown: bool = False

        self.started_at: Optional[datetime] = None

        self.last_event_type: Optional[str] = None
        self.last_event_source: Optional[str] = None
        self.last_event_time: Optional[datetime] = None

        self.event_count: int = 0
        self.event_types: Dict[str, int] = {}

        self.modules_ready: Set[str] = set()

    def update_from_event(self, event: Event):
        """
        Update context state based on incoming event.
        """

        self.last_event_type = event.type
        self.last_event_source = event.source
        self.last_event_time = event.timestamp

        self.event_count += 1
        self.event_types[event.type] = (
            self.event_types.get(event.type, 0) + 1
        )

        # system lifecycle signals
        if event.type == "SYSTEM_START":
            self.system_started = True
            self.started_at = event.timestamp

        elif event.type == "SYSTEM_SHUTDOWN":
            self.system_shutdown = True

        # module readiness signal
        elif event.type.endswith("_READY"):
            self.modules_ready.add(event.source)

            # örnek politika:
            if len(self.modules_ready) >= 1:
                self.system_ready = True