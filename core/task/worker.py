import time
from core.task.task_queue import TaskQueue

class Worker:
    """
    Single-threaded task worker.
    """

    def __init__(self, queue: TaskQueue, logger, poll_interval: float = 0.2):
        self.queue = queue
        self.logger = logger
        self.poll_interval = poll_interval
        self.running = False

    def start(self):
        self.running = True
        self.logger.info("WORKER", "Worker loop started")

        while self.running:
            task = self.queue.dequeue()

            if task:
                try:

                    if not hasattr(task, "logger") or task.logger is None:
                        task.logger = self.logger

                    self.logger.info("WORKER", f"Executing task: {task.__class__.__name__}")
                    task.start()
                   
                    self.logger.info("WORKER", f"Task completed: {task.__class__.__name__}")
                except Exception as e:
                    self.logger.error("WORKER", f"Task failed: {e}")
            else:
                time.sleep(self.poll_interval)

        self.logger.info("WORKER", "Worker loop stopped")

    def stop(self):
        self.running = False