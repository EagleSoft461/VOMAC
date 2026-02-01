from typing import Dict, Type
from core.task.task import Task

class TaskRegistry:
    """
    Central registry for all executable task types
    """ 

    def __init__(self):
        self.registry: Dict[str, Type[Task]] = {}

    def register (self, task_type: str, task_cls: Type[Task]):
        if task_type in self._registry:
            raise ValueError(f"Task already registered: {task_type}")
        
        if not issubclass(task_cls, Task):
            raise TypeError("Task must inherit from Task base class")
        
        self._registry[task_type] = task_cls

    def create(self, task_type: str, payload: dict) -> Task:
        if task_type not in self._registry:
            raise ValueError(f"Unknown task type: {task_type}")
        
        task_cls = self._registry[task_type]
        return task_cls(payload)
    
    def list_tasks(self):
        return list(self._registry.keys())