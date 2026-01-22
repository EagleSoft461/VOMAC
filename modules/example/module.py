from core.module_interface import ModuleInterface
from core.events.event import Event

class Module(ModuleInterface):
    def init(self, core):
        self.core = core
        core.logger.info("EXAMPLE", "Module initialized")

        # Emit example event
        self.core.dispatcher.emit(
            Event(
                type="EXAMPLE_READY",
                source="example",
                payload={
                    "status": "ready"
                }
            )
        )

    def on_event(self, event):
        self.core.logger.info(
            "EXAMPLE",
            f"Event received: {event.type} from {event.source}"
        )

    def shutdown(self):
        self.core.logger.info("EXAMPLE", "Module shutting down")