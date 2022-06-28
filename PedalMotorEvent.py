from abc import abstractmethod
from abc import ABC

class PedalMotorEvent(ABC):
        
    @abstractmethod
    def pressing(self, motorPin, cycle, motor, name):
        pass
    
    @abstractmethod    
    def unpressing(self, motorPin, cycle, motor, name):
        pass
        

    