from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional
import uuid

class TaskStatus(Enum):
    CREATED = "CREATED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

@dataclass
class TaskMetadata:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: TaskStatus = TaskStatus.CREATED
    created_at: datetime = field(default_factory=datetime.utcnow)
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None

class Task(ABC):
    """
    Base class for all system tasks.

    A Task represents a single unit of executable work.

    Tasks are:
    - stateless
    - deterministic
    - execution-focused

    Tasks do NOT manage:
    - scheduling
    - retries
    - workers
    - orchestration
    """

    def __init__(self, payload: Dict[str,Any]):
        self.payload = payload
        self.meta = TaskMetadata()

    def start(self):
        self.meta.status = TaskStatus.RUNNING
        self.meta.started_at = datetime.utcnow()

        try:
            result = self.execute()
            self.complete()
            return result
        
        except Exception as e:
            self.fail()
            raise e
        
    def complete(self):
        self.meta.status = TaskStatus.COMPLETED
        self.meta.finished_at = datetime.utcnow()

    def fail(self):
        self.meta.status = TaskStatus.FAILED
        self.meta.finished_at = datetime.utcnow()

    @abstractmethod
    def execute(self):
        """
        Actual task logic must be implemented here.
        """
        pass