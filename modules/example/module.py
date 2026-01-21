from core.module_interface import ModuleInterface

class Module(ModuleInterface):
    def init(self, core):
        self.core = core
        core.logger.info("EXAMPLE", "Module initialized")

    def shutdown(self):
        self.core.logger.info("EXAMPLE", "Module shutting down")