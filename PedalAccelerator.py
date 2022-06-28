from Pedal import Pedal
from MotorPedalConfig import MotorPedalConfig

class PedalAccelerator(Pedal):
       
    @classmethod   
    def ACCELERATOR(self):
        return 'accelerator'
           
    def __init__(self, eventMotorController):
        CYCLE_PRESS = 5
        CYCLE_UNPRESS = 7
        PEDAL_PIN = 7
    
        Pedal.__init__(self, PEDAL_PIN, CYCLE_PRESS, CYCLE_UNPRESS, MotorPedalConfig(), eventMotor=eventMotorController, motorName=self.ACCELERATOR())
        
    
