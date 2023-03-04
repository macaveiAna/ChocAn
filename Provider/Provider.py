from Member import *
import random
import os
from pathlib import Path

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
        self.add_provider()
    
    def print_exists(self):
        print("Provider already exists.")  
    #test
    def add_provider(self):
        cwd = os.getcwd() #gets current working directory
        parent_dir = "/ChocAn/Provider/" #sets relative path in variable
        
        #If provider already has a file, will print a statement that it exists
        if os.path.exists(f"{cwd}/{parent_dir}/{self.provider_name}"): 
            self.print_exists()
        else:
            #creates the new provider directory
            directory = f"{self.provider_name}/" #new provider directory
            p = Path(f"ChocAn/Provider/{directory}/") #sets path to the new provider's directory
            p.mkdir() #makes the directory
            #contents for file that is uploaded
            provider = {
                    "ProviderName": self.provider_name,
                    "ProviderID": self.provider_id,
                    "ProviderAddr": self.strAddr,
                    "ProviderCity": self.city,
                    "ProviderState": self.state,
                    "ProviderZip": self.zip,
                    "Services": [{
                        
                    }]
            }
            #Opens the path to the new folder and creates new json file for provider profile        
            with open(f"{p}/{self.provider_name}.json",mode="w") as file:   #file 
               json.dump(provider,file,indent= 4)

            #Opens the path to the Provider folder for the
            # list of providers in the json file
            with open(f"{cwd}/{parent_dir}/ProviderList.json",mode="r") as file:
                data = json.load(file)
            #New provider data for the json file containing all providers in Provider folder
            new_provider = {
                "ProviderName": self.provider_name,
                "ProviderId": self.provider_id
            }
            #Appends the new provider to the full provider list
            data['providers'].append(new_provider)
            with open(f"{cwd}/{parent_dir}/ProviderList.json",mode="w") as file:
                json.dump(data,file,indent= 4)
            
            
    #test
    def remove_provider(self):
        id = self.getProviderID()
        with open("Provider/ProviderList.json",mode="r") as file:
            data = json.load(file)
        for index,provider in enumerate(data['providers']):
            if provider['ProviderId'] == id:
                data['providers'].pop(index)
        with open("Provider/ProviderList.json",mode="w") as file:
            json.dump(data,file, indent = 4)    
    #test
    def update_provider(self):
        pass
    
    def getProviderID(self):
        print("\nPlease enter a valid provider ID number.")
        id = input("> ")

        if len(id) != 9 or id.isnumeric() == False:
            return self.getProviderID()
        else:
            return id
        
    def printWelcomeMessage(self, name):
        print("Welcome ", name)
        
    #test
    def getProviderName(self,id):
        with open("Provider/ProviderList.json",mode="r") as file:
            data = json.load(file)
        for member in data['providers']:
            if member['ProviderId'] == id:
                name = member["ProviderName"]
                self.printWelcomeMessage(name)
                return name
        return None
                
    
    #test
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
                
            with open("Service/ProviderDirectory.json") as file:
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
        with open("Service/ProviderDirectory.json") as file:
            data = json.load(file)
        for service in data['services']:
            if service['serviceCode'] == service_code:
                name = service['serviceName']
                validServiceCode = True
                self.printServiceName(name)
                break
        if(validServiceCode == False):
            print("Invalid service code")
    
    #test 
    def load(self):
        self.provider_id = self.getProviderID()
        self.provider_name = self.getProviderName(self.provider_id)
        while(self.provider_name == None):
            print("Invalid Provider Id")
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
            