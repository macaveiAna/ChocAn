        
class Manager:
    pass

class Provider:
    def __init__(self):
        self.provider_id = 0
        self.provider_name = ""
    #pass

class Member:
 
    def __init__(self):
        self.member_id = 0
        self.member_name = ""
        
    #first check in main function if member already exits
    def add_member(self, member_id, member_name):
        with open("MemberDirectory.txt", "a") as file:
            file.write(member_id)
            file.write(member_name)
        file.close()
    
    #function to read in user input
    def validate_member(self):
        self.member_id = input("Please enter your 9 digit member ID: ")
        print("\n\n")
        self.member_name = input("Please enter your 9 digit member ID: ")
        
    def remove_member(self):
        pass
        
        
        
    #function to compare what is in the file
    

class Services:
    pass


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

    def getProviderID(self):
        print("\nPlease enter a valid provider ID number.")
        id = input("> ")

        if len(id) != 9 or id.isnumeric() == False:
            return self.getProviderID()
        else:
            return id

    def getProviderName(self,id):
        '''
        print("\nPlease enter a valid provider name.")
        name = input("> ")

        if name.isalpha() == False:
            return self.getProviderName()
        else:
            return name
        '''
        with open("Provider/ProviderList.txt",mode="r") as file:
            if(file.read() == id):
                return id

    def loadTerminal(self):
        print("\n\nWelcome to ChocAn!\n")
        print("Enter 1 if you are a Provider.")
        print("Enter 2 if you are a Manager.")

        choice = self.getInitInput()
        self.setType(choice)

        if self.type == "Provider": # if type is provider
            #provider code
            provider = Provider() # dec
            provider.provider_id = self.getProviderID()
            provider.provider_name = self.getProviderName(id)
            print("Welcome ",provider.provider_name)

        else: # if type is manager
            #manager code
            pass