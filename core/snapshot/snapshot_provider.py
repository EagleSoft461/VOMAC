from abc import ABC, abstractmethod
from typing import Dict, Any

class SnapshotProvider(ABC):
    @abstractmethod
    def get_snapshot(self) -> Dict[str, Any]:
        pass