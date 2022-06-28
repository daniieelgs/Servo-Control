import json

class JSONController:
    
    def __init__(self, nameFile):
        self.file = nameFile
        
    def getRegisterPedal(self, pedalName):
        with open(self.file) as file:
            data = json.load(file)
            
            return data[pedalName]  
    
    def setRegisterPedal(self, dataPedal):
        pass
    
    def setRegister(self, data):
        print("SAVING: ")
        print(data)
        with open(self.file, 'w') as file:
            json.dump(data, file, indent=4)
        
    