from collections import deque
from typing import Optional
from core.task.task import Task

class TaskQueue:
    """
    In-memory FIFO task queue.
    """

    def __init__(self):
        self._queue = deque()

    def enqueue(self, task: Task):
        self._queue.append(task)

    def dequeue(self) -> Optional[Task]:
        if self.is_empty():
            return None
        return self._queue.popleft()
    
    def is_empty(self) -> bool:
        return len(self._queue) == 0
    
    def size(self) -> int:
        return len(self._queue)