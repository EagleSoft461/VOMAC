from core.task.task_registry import TaskRegistry
from core.task.task_queue import TaskQueue
from core.task.task_manager import TaskManager
from core.task.worker import Worker
import threading


class ExecutionEngine:
    def __init__(self, logger):
        self.logger = logger

        self.registry = TaskRegistry()
        self.queue = TaskQueue()
        self.manager = TaskManager(self.registry, self.queue)

        self.worker = Worker(self.queue)
        self.worker_thread = None

    def start(self):
        self.logger.info("ENGINE", "Execution engine starting")

        self.worker_thread = threading.Thread(
            target=self.worker.start,
            daemon=True
        )
        self.worker_thread.start()

        self.logger.info("ENGINE", "Worker started")

    def stop(self):
        self.logger.info("ENGINE", "Execution engine stopping")

        self.worker.stop()

        if self.worker_thread:
            self.worker_thread.join()

        self.logger.info("ENGINE", "Execution engine stopped")