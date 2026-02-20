from typing import List
from core.events.event import Event

class MemoryStore:
    """
    In-memory event history store.

    This class is intentionally simple.
    It provides append-only storage for system events
    during a single execution lifecycle.
    """

    MAX_EVENTS = 1000

    def __init__(self):
        self._events: List[Event] = []

    def append(self, event: Event) -> None:
        """
        Store an event snapshot in memory.

        Oldest events are discarded if MAX_EVENTS is exceeded.
        """
        self._events.append(event)

        if len(self._events) > self.MAX_EVENTS:
            self._events.pop(0)

    def get_all(self) -> List[Event]:
        """
        Return a copy of all stored events.
        """
        return list(self._events)
    
    def snapshot(self) -> dict:
        """
        Return a serializable snapshot of current memory state.
        """
        return {
            "event_count": len(self._events),
            "last_event_type": self._events[-1].type if self._events else None,
            "recent_events": [e.type for e in self._events[-10:]],
            "max_events": self.MAX_EVENTS
        }
    
    def clear(self) -> None:
        """
        Clear all memory contents.
        """
        self._events.clear()