
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

    def loadTerminal(self):
        print("\n\nWelcome to ChocAn!\n")
        print("Enter 1 if you are a Provider.")
        print("Enter 2 if you are a Manager.")

        choice = self.getInitInput()
        self.setType(choice)
        
class Manager:
    pass

class Provider:
    pass

class Member:
    
    def __init__(self, member_id):
        self.member_id = member_id
        
    #first check in main function if member already exits
    def add_member(self):
        pass
    
    #function to read in user input
    def validate_member(self):
        self.member_id = input("Please enter your 9 digit member ID: ")
        print("\n\n")
        
    #function to compare what is in the file
        

class Services:
    pass