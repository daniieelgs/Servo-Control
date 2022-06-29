from PinnerConfiguration import PinnerConfiguration
import RPi.GPIO as GPIO

class LedConfig(PinnerConfiguration):
    
    def __init__(self, ledPin, GPIOMode = GPIO.BOARD):
        PinnerConfiguration.__init__(self, ledPin, GPIOMode=GPIOMode)
        
    def pinConfig(self):
        GPIO.setmode(self.GPIOMode)
        GPIO.setup(self.channel, GPIO.OUT)
    
    def disable(self):
        GPIO.setmode(self.GPIOMode)
        GPIO.output(self.channel, GPIO.LOW)
        GPIO.cleanup(self.channel)