from core.module_interface import ModuleInterface
from core.events.event import Event

class Module(ModuleInterface):

    def init(self, core):
        self.core = core
        core.dispatcher.subscribe(self)
        core.logger.info("EXAMPLE", "Module initialized")

        # örnek event
        core.dispatcher.emit(
            Event(
                type="EXAMPLE_READY",
                source="example",
                payload={}
            )
        )

    def on_event(self, event: Event):
        pass

    def shutdown(self):
        self.core.logger.info("EXAMPLE", "Module shutting down")