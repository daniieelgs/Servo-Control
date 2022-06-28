from Pedal import Pedal
from MotorPedalConfig import MotorPedalConfig

class PedalBreak(Pedal):
    
    @classmethod   
    def BREAK(self):
        return 'break'
    
    def __init__(self, eventMotorController):
        CYCLE_PRESS = 3
        CYCLE_UNPRESS = 5
        PEDAL_PIN = 11
    
        Pedal.__init__(self, PEDAL_PIN, CYCLE_PRESS, CYCLE_UNPRESS, MotorPedalConfig(), eventMotor=eventMotorController, motorName=self.BREAK())