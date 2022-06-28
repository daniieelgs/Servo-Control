from LoggerPedal import LoggerPedal
from JSONController import JSONController
import os

class FileLoggerPedal(LoggerPedal):
    
    def __init__(self, nameFile, *nameRegisters):
        self.__nameFile = nameFile
        self.__json = JSONController(nameFile)
        self.data = {}
        self.cursor = {}
        self.printLog = True
        self.writable = True
        
        for n in nameRegisters:
            self.cursor[n] = 0
        
        if not os.path.exists(nameFile):
            for n in nameRegisters: self.data[n] = []
            self.__json.setRegister(self.data)
        else:
            print("READING")
            for n in nameRegisters:
                self.data[n] = self.__json.getRegisterPedal(n)
                
        print(self.data)        

        
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
     
    def setWritable(self, enable):
        self.writable = enable 
        
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