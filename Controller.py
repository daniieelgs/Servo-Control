import RPi.GPIO as GPIO
from ButtonsConfig import ButtonsConfig
from PedalAccelerator import PedalAccelerator
from PedalBreak import PedalBreak
from PedalEventLogger import PedalEventLogger
from FileLoggerPedal import FileLoggerPedal
import time

BUTTON_ACCELERATOR = 10
BUTTON_BREAK = 8

GPIO.setwarnings(False)

ACCELERATOR = PedalAccelerator.ACCELERATOR()
BREAK = PedalBreak.BREAK()

nameFile = "logPedals.json"
logPedal = FileLoggerPedal(nameFile, ACCELERATOR, BREAK)
eventPedalAcc = PedalEventLogger(logPedal, printLog=False)
eventPedalBr = PedalEventLogger(logPedal, printLog=False)

#logPedal.setPrintLog(False)
#logPedal.setWritable(False)

button_pedal = {
    BUTTON_ACCELERATOR : PedalAccelerator(eventPedalAcc),
    BUTTON_BREAK : PedalBreak(eventPedalBr)
    }

write = False

def writeMode():
    global write
    write = True  
    
def readMode():
    global write
    write = False

lastPushed = {}

def callback_event_button(channel):
    
    if not channel in lastPushed.keys():
        lastPushed[channel] = -1
    
    if GPIO.input(channel) == lastPushed[channel]: return
    
    if GPIO.input(channel) == GPIO.HIGH:
        button_pedal[channel].press()
    else:
        button_pedal[channel].unpress()
        
    lastPushed[channel] = GPIO.input(channel)

def startPins():
        
    global write
        
    mode = "Write" if write else "Read"    
    print(f"{mode} Mode")   
        
    conf = ButtonsConfig(callback=callback_event_button) if write else ButtonsConfig()
    
    conf.pinConfig(BUTTON_ACCELERATOR)
    conf.pinConfig(BUTTON_BREAK)
    
    
def execute():
    if write: return False
    
    logPedal.setPrintLog(False)
    logPedal.setWritable(False)
    
    countAccelerator = time.time()
    countBreak = time.time()
    
    timeAccelerator = 0
    timeBreak = 0
    
    pressAccelerator = False
    pressBreak = False
    
    endAccelerator = False
    endBreak = False
    
    while not endAccelerator or not endBreak:
    
        now = time.time()
        
        elapsed = now - countAccelerator
                
        if not endAccelerator and elapsed >= timeAccelerator:
            
            data = logPedal.nextStep(ACCELERATOR)
            
            if not data:
                endAccelerator = True
                print('Accelerator end')
            
            else:           
                pressAccelerator, timeAccelerator = data
                button_pedal[BUTTON_ACCELERATOR].press() if pressAccelerator else button_pedal[BUTTON_ACCELERATOR].unpress()
                countAccelerator = now
                print(f"Accelerator -> Press: {pressAccelerator} - Time: {timeAccelerator}")
            
            
            
        elapsed = now - countBreak
        
        if not endBreak and elapsed >= timeBreak:
            
            data = logPedal.nextStep(BREAK)
            
            if not data:
                endBreak = True
                print("Break End")
            
            else:                
                pressBreak, timeBreak = data
                button_pedal[BUTTON_BREAK].press() if pressBreak else button_pedal[BUTTON_BREAK].unpress()
                countBreak = now
                print(f"Break -> Press: {pressBreak} - Time: {timeBreak}")
                    
    
    
def exit():
    if write: logPedal.save()
    for k in button_pedal:
        button_pedal[k].dissable()
    GPIO.cleanup()
    
    
    