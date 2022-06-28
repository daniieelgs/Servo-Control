from PedalMotorEvent import PedalMotorEvent
import time

class PedalEventLogger(PedalMotorEvent):
    
    def __init__(self, logPedal, printLog = False):
        self.__log = logPedal
        self.__timerPress = self.__time()
        self.__timerUnpress = self.__time()
        self.__printer = printLog
        
    def pressing(self, motorPin, cycle, motor, name):
        self.__timerPress = self.__time()
        
        timeElapsed = self.__time() - self.__timerUnpress
        self.__timerUnpress = self.__time()
        self.__log.registerUnpress(name, timeElapsed)
        if self.__printer: print(f"Pressing '{name}' End: {self.__time()} - Begin: {self.__timerUnpress} Elapsed: {timeElapsed}")
        
    def unpressing(self, motorPin, cycle, motor, name):
        
        self.__timerUnpress = self.__time()
                
        timeElapsed = self.__time() - self.__timerPress
        self.__timerPress = self.__time()
        self.__log.registerPress(name, timeElapsed)
        if self.__printer: print(f"Unpressing '{name}' End: {self.__time()} - Begin: {self.__timerPress} Elapsed: {timeElapsed}")
        
    def __time(self):
        return time.time()