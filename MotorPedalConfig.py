from PinnerConfiguration import PinnerConfiguration
import RPi.GPIO as GPIO
import time

class MotorPedalConfig(PinnerConfiguration):
    
    def pinConfig(self, channel):
        channel = int(channel)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(channel, GPIO.OUT)
        p = GPIO.PWM(channel, 50)
        self.__motor = p
        p.start(12)
        p.ChangeDutyCycle(12)
        return p
    
    def disable(self, channel):
        GPIO.setmode(GPIO.BOARD)
        self.__motor.ChangeDutyCycle(12)
        time.sleep(0.2)
        GPIO.cleanup(channel)