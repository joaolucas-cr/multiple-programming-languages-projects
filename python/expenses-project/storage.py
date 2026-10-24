import json 
from sys import exit


class Storage:
    storageFilename = "expenses.json"

    def initialValidation(self):
        try:
            with open(f"./{self.storageFilename}", "r") as file:
                json.load(file)
        except FileNotFoundError:
            print("FILE NOT FOUND")
            exit()
        except: 
            print("ERROR EXEPNSES JSON CORRUPTED -- EXITING")
            exit()
    
    def __init__(self):
        self.initialValidation()

    def getBudget(self):
        try:
            with open(f"./{self.storageFilename}", "r") as file:
                storage = json.load(file)
                return storage['budget']
        except FileNotFoundError:
            print("FILE NOT FOUND")
            exit()
        except: 
            print("ERROR EXEPNSES JSON CORRUPTED -- EXITING")
            exit()

    def getExpense(self): 
        try:
            with open(f"./{self.storageFilename}", "r") as file:
                storage = json.load(file)
                return storage['expenses']
        except Exception as error:
            raise ValueError(error)

    def saveExpenses(self, expenses): 
        try:
            with open(f"./{self.storageFilename}", "r") as file:
                storage = json.load(file)
                storage['expenses'] = [expense.toDict() for expense in expenses]
                with open(f"./{self.storageFilename}", "w") as writeFile:
                    json.dump(storage, writeFile, indent=True)
        except Exception as error:
            raise ValueError(error)
            
    def updateBudget(self, value):
        try:
            with open(f"./{self.storageFilename}", "r") as file:
                storage = json.load(file)
                storage['budget'] = value
                with open(f'./{self.storageFilename}', "w") as writeFile:
                    json.dump(storage, writeFile, indent=True)
        except FileNotFoundError:
            print("FILE NOT FOUND")
            exit()
        except: 
            print("ERROR EXEPNSES JSON CORRUPTED -- EXITING")
            exit()