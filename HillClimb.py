import RPi.GPIO as GPIO
import time
from PedalAccelerator import PedalAccelerator
from PedalBreak import PedalBreak
import Controller

#Controller.readMode()
Controller.writeMode()  
Controller.startPins()

try:
    #Controller.execute()
    input("\nEnter to exit\n")
    Controller.exit()

except KeyboardInterrupt:
    pass
finally:
    Controller.exit()
