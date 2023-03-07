from Provider import Provider
from Member import *
import json
import random
import pandas as pd
from tabulate import tabulate

class Service:
    def __init__(self):
        self.service_name = ""
        self.service_code = ""
        self.service_fee = ""

    def load_file(self):
        with open("Service/ProviderDirectory.json", "r") as file:
            data = json.load(file)
        return data
    
    def write_to_file(self,data):
        with open("Service/ProviderDirectory.json","w") as file:
            json.dump(data, file, indent=4)
    
    def enter_service_details(self):
        print("Please enter name of service: ")
        self.service_name = input("> ")
        for i in range(6):
            self.service_code += str(random.randint(0,9))
        print("Please enter service fee: ")
        self.service_fee = input("> ")
        self.add_service()
        
    def add_service(self):
        data = self.load_file()
        new_service = {
            "serviceName": self.service_name,
            "serviceCode": self.service_code,
            "servicePrice": "$" + self.service_fee
        }
        data['services'].append(new_service)
        self.write_to_file(data)
    
    def print_not_found(self):
        print("Service not found")

    def remove_service(self):
        self.display_services()
        found = False
        service_code = self.getServiceCode()
        sName = self.getServiceName(service_code)
        if sName != None:
            found = True
        else:
            self.print_not_found()
        
        data = self.load_file()
        for index,service in enumerate(data['services']):
            if service['serviceCode'] == service_code:
                data['services'].pop(index)
                found = True
        
        self.write_to_file(data)   
        return found
    
    def update_service_fee(self):
        self.display_services()
        sCode = self.getServiceCode()
        print("Enter the new price for the service:")
        new_price = input("> ")
        
        data = self.load_file()
        for service in data['services']:
            if service['serviceCode'] == sCode:
                service['servicePrice'] = "$" + new_price
        
        self.write_to_file(data)

    def display_services(self):
        # Load the JSON data
        data = self.load_file()
        # Convert the data to a DataFrame
        df = pd.DataFrame(data['services'])
        df_styled = df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'left'})
        print("List of Services")
        print(tabulate(df_styled.data, headers=df_styled.columns, tablefmt='grid', showindex=False))

    def update_service_name(self):
        self.display_services()
        sCode = self.getServiceCode()
        print("Enter the new name for the service:")
        new_name = input("> ")
        data = self.load_file()
        for service in data['services']:
            if service['serviceCode'] == sCode:
                service['serviceName'] = new_name
        self.write_to_file(data)

    def getServiceCode(self):
        print("\nPlease enter a valid service code.")
        code = input("> ")
        if len(code) != 6 or code.isnumeric() == False:
            return self.getServiceCode()
        else:
            return code
        
    def getServiceName(self,code):
        data = self.load_file()
        for service in data['services']:
            if service['serviceCode'] == code:
                sName = service["serviceName"]
                return sName
        return None
    
    def validateServiceName(self,member_id,date,name,pName,member_name,service_code):
        p = Provider.Provider()
        m = Member()
        print("Is this the correct service that was provided? ","'",name,"'","[y/n]")
        ans = input("> ")
        if(ans == 'y'):   
            data = self.load_file()
            for service in data['services']:
                if service['serviceName'] == name:
                    fees = service['servicePrice']
                    print("Here is the total amount due: ", fees)
                    break
            
        elif(ans == 'n'):
            print("Try again!")
            p.load_validated(member_id, member_name, date)
        else:
            print("Invalid response!")
    
    def printServiceName(self,sname):
            print("Service: ", sname)
            
    