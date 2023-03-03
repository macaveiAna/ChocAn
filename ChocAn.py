
from Provider import *
from Manager import *

class Terminal:
    def __init__(self):
        self.type = ""
    
    def getInitInput(self):
        choice = int(input("> "))
        if choice != 1 and choice != 2:
            print("Please enter valid choice.")
            self.getInitInput()
        
        return choice

    def setType(self, choice):
        if choice == 1:
            self.type = "Provider"
        else:
            self.type = "Manager"

        return self.type
        
    def getMemberID(self):
        print("\nPlease enter a valid member ID number.")
        id = input("> ")
        if len(id) != 9 or id.isnumeric() == False:
            return self.getMemberID()
        else:
            return id
        
    def loadTerminal(self):
        print("\n\nWelcome to ChocAn!\n")
        print("Enter 1 if you are a Provider.")
        print("Enter 2 if you are a Manager.")

        choice = self.getInitInput()
        self.setType(choice)

        if self.type == "Provider": # if type is provider
            provider = Provider()
            provider.load()
            
        else: # if type is manager
            manager = Manager()
            manager.load()