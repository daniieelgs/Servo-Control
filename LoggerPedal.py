from abc import abstractmethod
from abc import ABC

class LoggerPedal(ABC):
    
    @abstractmethod
    def registerPress(self, name, timer):
        pass
    
    @abstractmethod
    def registerUnpress(self, name, timer):
        pass
    
    @abstractmethod
    def save(self):
        pass 
    