from core.task.worker import Worker
from core.task.task_queue import TaskQueue
import threading

class ExecutionEngine:
    def __init__(self, logger, queue: TaskQueue):
        self.logger = logger
        self.queue = queue

        self.worker = Worker(self.queue, logger=self.logger)
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