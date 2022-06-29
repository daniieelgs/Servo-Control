from Pedal import Pedal
from MotorPedalConfig import MotorPedalConfig
from DriverLed import DriverLed
from LedConfig import LedConfig

class PedalAccelerator(Pedal):
       
    @classmethod   
    def ACCELERATOR(self):
        return 'accelerator'
           
    def __init__(self, eventMotorController):
        CYCLE_PRESS = 8
        CYCLE_UNPRESS = 10
        PEDAL_PIN = 7
    
        Pedal.__init__(self, CYCLE_PRESS, CYCLE_UNPRESS, MotorPedalConfig(PEDAL_PIN), driverLed = DriverLed(LedConfig(37)),eventMotor=eventMotorController, motorName=self.ACCELERATOR())
        
    
