from abc import abstractmethod
from abc import ABC

class PinnerConfiguration(ABC):
    
    @abstractmethod
    def pinConfig(self, channel):
        pass
    
    @abstractmethod
    def disable(self, channel):
        pass