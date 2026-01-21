from abc import ABC, abstractmethod

class ModuleInterface(ABC):

    @abstractmethod
    def init(self, core):
        """
        Called once during system startup.
        """
        pass

    @abstractmethod
    def shutdown(self):
        """
        Called once during system shutdown.
        """
        pass