import RPi.GPIO as GPIO

class Pedal:
    def __init__(self, motorPin, cyclePress, cycleUnpress, pinnerConf, ledPin = None, motorName = None, eventMotor = None):
        self.__motorPin = motorPin
        self.__cyclePress = cyclePress
        self.__cycleUnpress = cycleUnpress
        self.__pinnerConf = pinnerConf
        self.__motor = pinnerConf.pinConfig(motorPin)
        self.__ledPin = ledPin
        self.__motorName = motorName
        self.__eventMotor = eventMotor
        self.__motor.ChangeDutyCycle(self.__cycleUnpress)
    
        
    def press(self):
        self.__motor.ChangeDutyCycle(self.__cyclePress)
        self.__moving(self.__cyclePress)
    
    def unpress(self):
        self.__motor.ChangeDutyCycle(self.__cycleUnpress)
        self.__moving(self.__cycleUnpress)
        
    def __moving(self, cycle):
        controller = self.__eventMotor
        
        if controller != None:
            if cycle == self.__cyclePress: controller.pressing(self.__motorPin, cycle, self.__motor, self.__motorName)    
            elif cycle == self.__cycleUnpress: controller.unpressing(self.__motorPin, cycle, self.__motor, self.__motorName)    
        
    def dissable(self):
        self.__pinnerConf.disable(self.__motorPin)