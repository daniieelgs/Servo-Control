import RPi.GPIO as GPIO

class Pedal:
    def __init__(self, cyclePress, cycleUnpress, motorConf, driverLed = None, motorName = None, eventMotor = None):
        self.__cyclePress = cyclePress
        self.__cycleUnpress = cycleUnpress
        self.__motorConf = motorConf
        self.__motor = motorConf.pinConfig()
        self.__driverLed = driverLed
        self.__motorName = motorName
        self.__eventMotor = eventMotor
        self.__motor.ChangeDutyCycle(self.__cycleUnpress)
    
        
    def press(self):
        self.__motor.ChangeDutyCycle(self.__cyclePress)
        self.__moving(self.__cyclePress)
        if self.__driverLed != None: self.__driverLed.on()
    
    def unpress(self):
        self.__motor.ChangeDutyCycle(self.__cycleUnpress)
        self.__moving(self.__cycleUnpress)
        if self.__driverLed != None: self.__driverLed.off()
        
    def __moving(self, cycle):
        controller = self.__eventMotor
        
        if controller != None:
            if cycle == self.__cyclePress: controller.pressing(self.__motorConf.channel, cycle, self.__motor, self.__motorName)    
            elif cycle == self.__cycleUnpress: controller.unpressing(self.__motorConf.channel, cycle, self.__motor, self.__motorName)    
        
    def dissable(self):
        self.__motorConf.disable()