from Pedal import Pedal
from MotorPedalConfig import MotorPedalConfig
from DriverLed import DriverLed
from LedConfig import LedConfig

class PedalBreak(Pedal):
    
    @classmethod   
    def BREAK(self):
        return 'break'
    
    def __init__(self, eventMotorController):
        CYCLE_PRESS = 3
        CYCLE_UNPRESS = 5
        PEDAL_PIN = 11
    
        Pedal.__init__(self, CYCLE_PRESS, CYCLE_UNPRESS, MotorPedalConfig(PEDAL_PIN), driverLed=DriverLed(LedConfig(35)), eventMotor=eventMotorController, motorName=self.BREAK())