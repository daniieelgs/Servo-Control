from abc import abstractmethod
from abc import ABC
import RPi.GPIO as GPIO

class PinnerConfiguration(ABC):

    def __init__(self, channel, GPIOMode = GPIO.BOARD):
        self.channel = int(channel)
        self.GPIOMode = GPIOMode
        

    @abstractmethod
    def pinConfig(self):
        pass
    
    @abstractmethod
    def disable(self):
        pass