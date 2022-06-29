from PinnerConfiguration import PinnerConfiguration
import RPi.GPIO as GPIO
import time

class MotorPedalConfig(PinnerConfiguration):
    
    def __init__(self, channel, defaultDutyCycle = 12, GPIOMode = GPIO.BOARD):
        PinnerConfiguration.__init__(self, channel, GPIOMode=GPIOMode)
        self.defaultDutyCycle = defaultDutyCycle
    
    def pinConfig(self):
        channel = self.channel
        GPIO.setmode(self.GPIOMode)
        GPIO.setup(channel, GPIO.OUT)
        p = GPIO.PWM(channel, 50)
        self.__motor = p
        p.start(self.defaultDutyCycle)
        p.ChangeDutyCycle(self.defaultDutyCycle)
        return p
    
    def disable(self):
        GPIO.setmode(self.GPIOMode)
        self.__motor.ChangeDutyCycle(self.defaultDutyCycle)
        time.sleep(0.2)
        GPIO.cleanup(self.channel)