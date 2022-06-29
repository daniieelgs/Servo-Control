import RPi.GPIO as GPIO
import time
from PedalAccelerator import PedalAccelerator
from PedalBreak import PedalBreak
import Controller

try:
    mode = input(">> ").lower()

    #Controller.readMode()
    if mode == 'w': Controller.writeMode()  
    Controller.startPins()
    
    if mode != 'w': Controller.execute()
    input("\nEnter to exit\n")
    Controller.exit()

except KeyboardInterrupt:
    pass
finally:
    Controller.exit()
