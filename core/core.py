from core.event_dispatcher import EventDispatcher
from core.module_loader import ModuleLoader
from core.config_manager import ConfigManager
from core.execution.engine import ExecutionEngine
from core.routing.task_router import TaskRouter
from core.task.task_registry import TaskRegistry
from core.task.task_queue import TaskQueue
from core.task.task_manager import TaskManager
from core.logger import Logger
from core.task.example_ready_task import ExampleReadyTask


class Core:
    def __init__(self):
        self.logger = Logger()

        # Core services
        self.config = ConfigManager()
        self.module_loader = ModuleLoader()

        # Event system
        self.dispatcher = EventDispatcher(self.logger)

        # Task system
        self.task_registry = TaskRegistry()
        self.task_queue = TaskQueue()
        self.task_manager = TaskManager(self.task_registry, self.task_queue)

        # Execution engine
        self.engine = ExecutionEngine(self.logger, self.task_queue)

        # Task routing (Event -> Task)
        self.task_router = TaskRouter(self.dispatcher, self.task_manager, self.logger)

        self.task_router.add_route(
            "EXAMPLE_READY",
            lambda event: {"task_name": ExampleReadyTask.NAME, "payload": {}}
        )

        self.task_router.start()

        self.modules = []

    def start(self):
        self.logger.info("CORE", "System starting")

        self.engine.start()

        module_names = self.module_loader.discover()

        for name in module_names:
            module = self.module_loader.load(name)
            module.init(self)

            # Subscribe module to events
            self.dispatcher.subscribe(module)
            self.modules.append(module)

        self.logger.info("CORE", "System started")

    def shutdown(self):
        self.logger.info("CORE", "System shutting down")

        for module in self.modules:
            module.shutdown()

        self.engine.stop()

        self.logger.info("CORE", "System stopped")