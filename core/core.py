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

from core.events.event import Event

from core.decision.decision_engine import DecisionEngine
from core.decision.rule import Rule
from core.decision.decision_result import DecisionResult


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

        # Decision layer (v0.5.0+)
        self.decision_engine = DecisionEngine(self.logger)

        # Demo rule (v0.5.1)
        self.decision_engine.register_rule(
            Rule(
                name="rule_example_ready_first_3",
                condition=lambda ctx: (
                    ctx.event_type == "EXAMPLE_READY"
                    and ctx.event_payload.get("i", 999) < 3
                ),
                action=lambda ctx: DecisionResult(
                    task_name=ExampleReadyTask.NAME,
                    payload=ctx.event_payload,
                    matched_rule="rule_example_ready_first_3",
                    evaluated_rules=[]
                )
            )
        )

        # Execution engine
        self.engine = ExecutionEngine(self.logger, self.task_queue)

        # v0.5.1 Snapshot provider registry
        self.snapshot_providers = {}

        # Task routing (Event -> Decision -> Task)
        self.task_router = TaskRouter(
            self.dispatcher,
            self.task_manager,
            self.decision_engine,
            self.logger,
            snapshot_providers=self.snapshot_providers
        )

        self.modules = []

    def start(self):
        self.logger.info("CORE", "System starting")

        # Start worker engine first
        self.engine.start()

        # Load modules
        module_names = self.module_loader.discover()

        for name in module_names:
            module = self.module_loader.load(name)
            module.init(self)

            # Subscribe module to events
            self.dispatcher.subscribe(module)
            self.modules.append(module)

            # v0.5.1 Snapshot provider registration
            if hasattr(module, "get_snapshot"):
                self.snapshot_providers[name] = module
                self.logger.info("CORE", f"Snapshot provider registered: {name}")

        # Start router AFTER modules are ready
        self.task_router.start()

        # Emit example events AFTER router started
        for i in range(5):
            self.dispatcher.emit(
                Event(
                    type="EXAMPLE_READY",
                    source="core",
                    payload={"i": i}
                )
            )

        self.logger.info("CORE", "System started")

    def shutdown(self):
        self.logger.info("CORE", "System shutting down")

        for module in self.modules:
            module.shutdown()

        self.engine.stop()

        self.logger.info("CORE", "System stopped")