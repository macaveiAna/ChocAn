import datetime
import json
from datetime import date, timedelta
from time import strptime

#generate different reports for provider and member
#able to add member,delete member, same with provider and able to also do the same with services  
class Manager:
    def __init__(self):
        pass
    def getOption(self):
        option = int(input("> "))
        if (option < 0 or option > 4):
            print("Please enter a valid option!")
            self.getOption()
        return option
    def menu(self):
        print("Welcome back!")
        print("Which service do you want?")
        print("1.Generate reports")
        print("2.Modify Members")
        print("3.Modify Providers")
        print("4.Modify Services")
        option = self.getOption()
        match option:
            case 1:
                print("Which report do you want to generate?")
                print("1.Member report")
                print("2.Provider report")
            case 2:
                print("What do you want to do?")
                print("1.Add member")
                print("2.Remove member")
                print("3.Update member records")
            case 3:
                print("What do you want to do?")
                print("1.Add provider")
                print("2.Remove provider")
                print("3.Update provider records")
            case 4:
                print("What do you want to do?")
                print("1.Add service")
                print("2.Remove service")
                print("3.Update services")
    def load(self):
        self.menu()
    

class Member:
 
    def __init__(self):
        self.member_id = ""
        self.member_name = ""
     
   
    #first check in main function if member already exits
    def add_member(self, member_id, member_name):
        today = date.today()
        #print(today)
       
        with open("Member/MemberDirectory.json", "r") as file:
            data = json.load(file)
        new_member = {
            "MemberName": member_name, 
            "MemberId": member_id, 
            "Status": "Active", 
            "last_payment": str(today)
            }
        data["members"].append(new_member)
        with open("Member/MemberDirectory.json", "w") as file:
            json.dump(data,file, indent = 4)
        
    def printSuspended(self):
        print("Fees are owed. Member suspended...")

    def isSuspended(self, member_id):

        with open("Member/MemberDirectory.json", "r") as file:
            data = json.load(file)
        
        for member in data['members']:
            if member['MemberId'] == member_id:
                date_obj = datetime.datetime.strptime(member["last_payment"], "%Y-%m-%d")
                date_obj = date_obj.date() + timedelta(days=30)
                

                if date.today() > date_obj:
                    # suspend this account
                    member['Status'] = 'Suspended'
                    return True
                else:
                    return False

        return False # default return. If trouble finding account
        

    
    #function to read in user input
    def validate_member(self, member_id): # Checks if member exists 
        with open('Member/MemberDirectory.json') as file:
            data = json.load(file)
        
        for member in data['members']:
            if member['MemberId'] == member_id:
                return True
        
        return False
    
    def pay_monthly_fee(self):
        pass
        
    #def remove_member(self):
        #pass
        
class Services:
    pass
class Provider:
    def __init__(self):
        self.provider_id = ""
        self.provider_name = ""
    
    def getProviderID(self):
        print("\nPlease enter a valid provider ID number.")
        id = input("> ")

        if len(id) != 9 or id.isnumeric() == False:
            return self.getProviderID()
        else:
            return id
        
    def printWelcomeMessage(self, name):
        print("Welcome ", name)
        

    def getProviderName(self,id):
        with open("Provider/ProviderList.json",mode="r") as file:
            data = json.load(file)
        for member in data['providers']:
            if member['ProviderId'] == id:
                name = member["ProviderName"]
                self.printWelcomeMessage(name)
                return name
                
    def getMemberID(self):
        print("\nPlease enter a valid member ID number.")
        id = input("> ")
        if len(id) != 9 or id.isnumeric() == False:
            return self.getMemberID()
        else:
            return id
    def validateServiceName(self,name):
        print("Is this the correct service that was provided? ","'",name,"'","[y/n]")
        ans = input("> ")
        if(ans == 'y'):
            print("Would you like to enter comments about the service provided? [y/n]")
            ans2 = input("> ")
            if ans2 == 'y':
                print("Please enter a comment (100 characters): ")
                comment = input("> ")
                filename = f"{self.provider_name}.json"
                with open(filename, "w") as file:
                    json.dump(comment, file)
                
            with open("Services/ProviderDirectory.json") as file:
                data = json.load(file)
            for service in data['services']:
                if service['serviceName'] == name:
                    fees = service['servicePrice']
                    print("Here is the total amount due: ", fees)
                    break
        elif(ans == 'n'):
            print("Try again!")
            self.load_validated()
        else:
            print("Invalid response!")
               
    def printServiceName(self,name):
            print("Service: ", name)
            self.validateServiceName(name)

      
    def load_validated(self):
        print("Please enter the date the service was provided:")
        date_service = input("> ")
        print("Please enter service code:")
        service_code = input("> ")
        validServiceCode = False
        with open("Services/ProviderDirectory.json") as file:
            data = json.load(file)
        for service in data['services']:
            if service['serviceCode'] == service_code:
                name = service['serviceName']
                validServiceCode = True
                self.printServiceName(name)
                break
        if(validServiceCode == False):
            print("Invalid service code")
        
    def load(self):
        self.provider_id = self.getProviderID()
        self.provider_name = self.getProviderName(self.provider_id)
        m = Member()
        m.member_id = self.getMemberID()
        var = m.validate_member(m.member_id)
        if var == True:
            if m.isSuspended(m.member_id) == True:
                m.printSuspended()
            else:
                print("Validated")
                self.load_validated()
        else:
            print("Invalid Number")
            



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