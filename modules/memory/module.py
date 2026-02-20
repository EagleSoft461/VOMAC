from core.module_interface import ModuleInterface
from core.events.event import Event
from .memory_store import MemoryStore


class Module(ModuleInterface):
    """
    Memory module.

    Observes system events and stores them
    as immutable history records.
    """

    def init(self, core):
        self.core = core
        self.store = MemoryStore()

        self.core.logger.info("MEMORY", "Memory module initialized")

    def on_event(self, event: Event):
        try:
            self.store.append(event)
            self.core.logger.info("MEMORY", f"Stored event: {event.type}")
        except Exception as e:
            self.core.logger.error("MEMORY", f"Failed to store event: {str(e)}")

    # v0.5.1 Snapshot support
    def get_snapshot(self):
        return self.store.snapshot()

    def shutdown(self):
        self.store.clear()
        self.core.logger.info("MEMORY", "Memory cleared on shutdown")