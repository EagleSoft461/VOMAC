from core.module_interface import ModuleInterface
from core.events.event import Event
from .context_state import ContextState

class Module(ModuleInterface):

    def init(self, core):
        self.core = core 
        self.state = ContextState()

        core.dispatcher.subscribe(self)

        core.logger.info("CONTEXT", "Context module initialized")

    def on_event(self, event: Event):
        self.state.update_from_event(event)

    def get_snapshot(self):
        return self.state.snapshot()
    
    def shutdown(self):
        self.core.logger.info("CONTEXT", "Context module shutdown")