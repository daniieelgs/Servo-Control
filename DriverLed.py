import RPi.GPIO as GPIO

class DriverLed:
    
    def __init__(self, ledConfig):
        ledConfig.pinConfig()
        self.conf = ledConfig
        
    def on(self):
        GPIO.output(self.conf.channel, GPIO.HIGH)
    
    def off(self):
        GPIO.output(self.conf.channel, GPIO.LOW)
    
    def disable(self):
        self.conf.disable()