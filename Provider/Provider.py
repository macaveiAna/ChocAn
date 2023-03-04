from Member import *
import random

class Provider:
    def __init__(self):
        self.provider_id = ""
        self.provider_name = ""
        self.strAddr = ""
        self.city = ""
        self.state = ""
        self.zip = ""
    
    def enter_Provider_details(self):
        print("Please enter provider's name: ")
        self.provider_name = input("> ")
        for i in range(9):
            self.provider_id += str(random.randint(0,9))
        print("Please enter the Street Address: ")
        self.strAddr = input("> ")
        print("Please enter the City: ")
        self.city = input("> ")
        print("Please enter the State: ")
        self.state= input("> ")
        print("Please enter the zipcode: ")
        self.zip = input("> ")
        self.add_provider(self.provider_name,self.provider_id)
        
    def add_provider(self,name,id):
        with open("Provider/ProviderList.json",mode="r") as file:
            data = json.load(file)
        new_provider = {
            "ProviderName": name,
            "ProviderId": id
        }
        data['providers'].append(new_provider)
        with open("Provider/ProviderList.json",mode="w") as file:
            json.dump(data,file,indent= 4)

    def remove_provider(self):
        id = self.getProviderID()
        with open("Provider/ProviderList.json",mode="r") as file:
            data = json.load(file)
        for index,provider in enumerate(data['providers']):
            if provider['ProviderId'] == id:
                data['providers'].pop(index)
        with open("Provider/ProviderList.json",mode="w") as file:
            json.dump(data,file, indent = 4)    
    
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
            m = Member()
            print("Try again!")
            m.load_validated()
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
        m.member_id = m.getMemberID()
        var = m.validate_member(m.member_id)
        if var == True:
            if m.isSuspended(m.member_id) == True:
                m.printSuspended()
            else:
                print("Validated")
                self.load_validated()
        else:
            print("Invalid Number")
            