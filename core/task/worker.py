import time
from core.task.task_queue import TaskQueue

class Worker:
    """
    Single-threaded task worker.
    """

    def __init__(self, queue: TaskQueue, poll_interval: float = 0.2):
        self.queue = queue
        self.poll_interval = poll_interval
        self.running = False

    def start(self):
        self.running = True

        while self.running:
            task = self.queue.dequeue()

            if task:
                task.start()
            else:
                time.sleep(self.poll_interval)

    def stop(self):
        self.running = False