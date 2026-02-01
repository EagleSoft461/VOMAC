from core.task.task_registry import TaskRegistry
from core.task.task_queue import TaskQueue
from core.task.task import Task

class TaskManager:
    """
    Responsible for task creation and scheduling.
    """

    def __init__(self, registry: TaskRegistry, queue: TaskQueue):
        self.registry = registry
        self.queue = queue
        pass

    def submit(self, task_name: str, payload: dict) -> Task:
        """
        Create a task and enqueue it.
        """
        task = self.registry.create(task_name, payload)
        self.queue.enqueue(task)
        return task