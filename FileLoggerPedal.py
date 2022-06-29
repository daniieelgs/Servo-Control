from LoggerPedal import LoggerPedal
from JSONController import JSONController
import os

class FileLoggerPedal(LoggerPedal):
    
    def __init__(self, nameFile, *nameRegisters, writable = False, printLog = True):
        self.__nameFile = nameFile
        self.__json = JSONController(nameFile)
        self.data = {}
        self.cursor = {}
        self.printLog = printLog
        self.writable = writable
        self.nameRegisters = nameRegisters
        
        for n in nameRegisters:
            self.cursor[n] = 0
        
        if not os.path.exists(nameFile) or self.writable:
            self.writeMode()
        else:
            self.readMode()
                
        print(self.data)        

    def readMode(self):
        print("READING")
        for n in self.nameRegisters:
            self.data[n] = self.__json.getRegisterPedal(n)
    
    def writeMode(self):
        print("WRITTING")
        for n in self.nameRegisters: self.data[n] = []
        self.__json.setRegister(self.data)       
        
    def setWritable(self, writable):
        self.writable = writable 
        self.writeMode() if writable else self.readMode()
        
    def registerPress(self, name, timer):
        if self.printLog: print(f"Pedal '{name} - Time: {timer} pressed")
        if self.writable: self.data[name].append({
            'press' : True,
            'time' : timer
        })
        
    def registerUnpress(self, name, timer):
        if self.printLog: print(f"Pedal '{name} - Time: {timer} unpressed'")
        if self.writable: self.data[name].append({
            'press' : False,
            'time' : timer
        })
    
    def setPrintLog(self, enable):
        self.printLog = enable
             
    def save(self):
        if self.writable:
            for i in self.data:
                self.data[i].append({
                    'press' : False,
                    'time' : 0
                })
            self.__json.setRegister(self.data)
            
    def nextStep(self, name):
        pedal = self.data[name]
                
        if self.cursor[name] >= len(pedal): return False
        
        stepPedal = pedal[self.cursor[name]]
        
        self.cursor[name] += 1
        
        return (stepPedal['press'], stepPedal['time'])