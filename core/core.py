from core.event_dispatcher import EventDispatcher
from core.module_loader import ModuleLoader
from core.config_manager import ConfigManager
from core.execution.engine import ExecutionEngine
from core.logger import Logger

class Core:
    def __init__(self):
        self.logger = Logger()

        self.config = ConfigManager()
        self.module_loader = ModuleLoader()
        self.dispatcher = EventDispatcher(self.logger)

        self.engine = ExecutionEngine(self.logger)
        self.modules = []

    def start(self):
        self.logger.info("CORE", "System starting")

        self.engine.start()

        module_names = self.module_loader.discover()
        
        for name in module_names:
            module = self.module_loader.load(name)
            module.init(self)
        self.dispatcher.subscribe(module)
        self.modules.append(module)

        self.logger.info("CORE", "System started")

    def shutdown(self):
        self.logger.info("CORE", "System shutting down")

        for module in self.modules:
            module.shutdown()

        self.engine.stop()

        self.logger.info("CORE", "System stopped")