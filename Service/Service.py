from Provider import Provider
import json
import random
import pandas as pd

class Service:
    def __init__(self):
        self.service_name = ""
        self.service_code = ""
        self.service_fee = ""
    
    def enter_service_details(self):
        print("Please enter name of service: ")
        self.service_name = input("> ")
        for i in range(6):
            self.service_code += str(random.randint(0,9))
        print("Please enter service fee: ")
        self.service_fee = input("> ")
        self.add_service()
        
    def add_service(self):
        with open("Service/ProviderDirectory.json", "r") as file:
            data = json.load(file)
        new_service = {
            "serviceName": self.service_name,
            "serviceCode": self.service_code,
            "servicePrice": self.service_fee
        }
        data['services'].append(new_service)
        with open("Service/ProviderDirectory.json","w") as file:
            json.dump(data, file, indent=4)
    
    def print_not_found(self):
        print("Service not found")

    def remove_service(self):
        found = False
        service_code = self.getServiceCode()
        sName = self.getServiceName(service_code)
        if sName != None:
            found = True
        else:
            self.print_not_found()
        with open("Service/ProviderDirectory.json",mode="r") as file:
            data = json.load(file)
        for index,service in enumerate(data['services']):
            if service['serviceCode'] == service_code:
                data['services'].pop(index)
                found = True
        with open("Service/ProviderDirectory.json",mode="w") as file:
            json.dump(data,file, indent = 4)    
        return found
    def update_service_fee(self):
        sCode = self.getServiceCode()
        print("Enter the new price for the service:")
        new_price = input("> ")
        with open("Service/ProviderDirectory.json",mode="r") as file:
            data = json.load(file)
        for service in data['services']:
            if service['serviceCode'] == sCode:
                service['servicePrice'] = "$" + new_price
        with open("Service/ProviderDirectory.json",mode="w") as file:
            json.dump(data,file, indent = 4)    

    def display_services(self):

        # Load the JSON data
        with open('Service/ProviderDirectory.json', 'r') as f:
            data = json.load(f)

        # Convert the data to a DataFrame
        df = pd.DataFrame(data['services'])

        # Display the DataFrame
        print(df.head())
    def update_service_name(self):
        pass
    def getServiceCode(self):
        print("\nPlease enter a valid service code.")
        code = input("> ")

        if len(code) != 6 or code.isnumeric() == False:
            return self.getServiceCode()
        else:
            return code
    def getServiceName(self,code):
        with open("Service/ProviderDirectory.json",mode="r") as file:
            data = json.load(file)
        for service in data['services']:
            if service['serviceCode'] == code:
                sName = service["serviceName"]
                return sName
        return None
    def validateServiceName(self,name):
        p = Provider.Provider()
        print("Is this the correct service that was provided? ","'",name,"'","[y/n]")
        ans = input("> ")
        if(ans == 'y'):   
            with open("Service/ProviderDirectory.json") as file:
                data = json.load(file)
            for service in data['services']:
                if service['serviceName'] == name:
                    fees = service['servicePrice']
                    print("Here is the total amount due: ", fees)
                    break
        elif(ans == 'n'):
            print("Try again!")
            p.load_validated()
        else:
            print("Invalid response!")
    
    def printServiceName(self,name):
            print("Service: ", name)
    