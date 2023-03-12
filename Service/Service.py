from Provider import Provider
from Member import *
from LLL import *
import json
import random
import pandas as pd
from tabulate import tabulate
from datetime import datetime

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
    def get_fee(self,sCode):
        data = self.load_file()
        fees = 0
        for service in data['services']:
            if service["serviceCode"] == sCode:
                fees = service['servicePrice']
        return fees
    def validateServiceName(self,sName, provider_number,provider_name, member_number,member_name, date_of_service):
        p = Provider.Provider()
        aLLL = RecordList()
        today = datetime.now()
        date_time_str = today.strftime("%Y-%m-%d %H:%M:%S")
        print("Is this the correct service that was provided? ","'",sName,"'","[y/n]")
        ans = input("> ")
        if(ans == 'y'):   
            data = self.load_file()
            comment = p.add_comments(provider_name)
            self.add_service_in_member_profile(provider_name, member_name, sName, date_of_service)
            for service in data['services']:
                code = service["serviceCode"]
                if service['serviceName'] == sName:
                    fees = service['servicePrice']
                    print("Here is the total amount due: ", fees)
                    break
            aLLL.add_record(date_time_str,date_of_service,provider_number,member_number,code,comment)
            aLLL.save_to_file("report/reports.txt")
            aLLL.display_records()
            self.add_service_in_provider_profile(provider_name,date_of_service,member_name,code,fees)
        elif(ans == 'n'):
            print("Try again!")
            p.load_validated(provider_name, date_of_service, member_name)
        else:
            print("Invalid response!")
    
    def add_service_in_member_profile(self, provider_name, member_name, service_name, date_of_service):
        with open(f"Member/{member_name}/{member_name}_profile.json", "r") as file:
            data = json.load(file)
        
        new_service = {
            "Date of Service ": str(date_of_service),
            "Provider Name ": provider_name,
            "Service Name ": service_name
        }
        
        data["Services"].append(new_service)
        with open(f"Member/{member_name}/{member_name}_profile.json", "w") as newfile:
            json.dump(data, newfile, indent = 4)
       
    def add_service_in_provider_profile(self,provider_name,date_of_service,member_name,service_code,service_fee):
        today = datetime.now()
        date_time_str = today.strftime("%Y-%m-%d %H:%M:%S")
        with open(f"Member/MemberDirectory.json", mode="r") as file:
            data = json.load(file)
        for member in data["members"]:
            if member["MemberName"] == member_name:
                member_number = member['MemberId']
        with open(f"Provider/{provider_name}/{provider_name}_profile.json", mode="r") as file:
            new_data = json.load(file)
        new_service = {
            "Date of Service ": str(date_of_service),
            "CurrentDate" : str(date_time_str),
            "MemberName" : member_name,
            "MemberNumber": member_number,
            "ServiceCode": service_code,
            "ServiceFee": service_fee
        }
        new_data["Services"].append(new_service)
        new_data["TotalConsultations"] += 1
        fee_str = new_data["TotalFee"]
        fee_str = fee_str.replace("$", "")
        service_fee_str = service_fee.replace("$", "")
        fee = float(fee_str) + float(service_fee_str)
        new_data["TotalFee"] = f"${fee:.2f}"
        with open(f"Provider/{provider_name}/{provider_name}_profile.json", "w") as newfile:
            json.dump(new_data, newfile, indent = 4)    
            
    
    
    def printServiceName(self,sname):
            print("Service: ", sname)
            
    