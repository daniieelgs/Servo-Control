import RPi.GPIO as GPIO
from PinnerConfiguration import PinnerConfiguration

class ButtonsConfig(PinnerConfiguration):
    
    def __init__(self, callback = None, event = GPIO.BOTH, pull_up_down = GPIO.PUD_DOWN):
        self.__callback = callback
        self.__event = event
        self.__pull_up_down = pull_up_down
    
    def pinConfig(self, channel):
        channel = int(channel)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(channel, GPIO.IN, pull_up_down=self.__pull_up_down)
        if self.__callback != None:
            GPIO.add_event_detect(channel, self.__event, callback=self.__callback)
    
    def disable(self, channel):
        GPIO.setmode(GPIO.BOARD)
        GPIO.cleanup(channel)
        