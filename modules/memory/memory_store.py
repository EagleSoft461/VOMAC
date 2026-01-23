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
    
    def clear(self) -> None:
        """
        Clear all memory contents.
        """
        self._events.clear()