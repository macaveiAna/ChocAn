import json
from Member import *
from Service import *
import random
import os
from pathlib import Path
import shutil
from tabulate import tabulate
from datetime import date, timedelta
import datetime


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
    
    def print_not_found(self):
        print("Provider does not exist.")
         
    #test
    def add_provider(self):

        today = date.today()
        cwd = os.getcwd() #gets current working directory
        parent_dir = "Provider" #sets relative path in variable
        
        #If provider already has a file, will print a statement that it exists
        if os.path.exists(f"{cwd}/{parent_dir}/{self.provider_name}"): 
            self.print_exists()
        else:
            #creates the new provider directory
            directory = f"{self.provider_name}/" #new provider directory
            '''
            p = Path(f"/ChocAn/Provider/{directory}") #sets path to the new provider's directory
            os.makedirs(p) #makes the directory
            '''
            path = os.getcwd() + "/Provider/" + directory
            os.makedirs(path)
            #contents for file that is uploaded
            provider = {
                    "ProviderName": self.provider_name,
                    "ProviderID": self.provider_id,
                    "ProviderAddr": self.strAddr,
                    "ProviderCity": self.city,
                    "ProviderState": self.state,
                    "ProviderZip": self.zip,
                    "Services": [
                        
                    ],
                    "TotalConsultations": 0,
                    "TotalFee": "$0.00"
            }
            #Opens the path to the new folder and creates new json file for provider profile        
            with open(f"{path}/{self.provider_name}_{str(today)}.json",mode="w") as file:   #file 
               json.dump(provider,file,indent= 4)

            #Opens the path to the Provider folder for the
            # list of providers in the json file
            
            with open(f"{cwd}/{parent_dir}/ProviderList.json",mode="r") as file:
                data = json.load(file)
                
            #New provider data for the json file containing all providers in Provider folder
            new_provider = {
                "ProviderName": self.provider_name,
                "ProviderId": self.provider_id,
                "ProviderAddr": self.strAddr,
                "ProviderCity": self.city,
                "ProviderState": self.state,
                "ProviderZip": self.zip,
            }
            #Appends the new provider to the full provider list
            data['providers'].append(new_provider)
            with open(f"{cwd}/{parent_dir}/ProviderList.json",mode="w") as file:
                json.dump(data,file,indent=4)
            
            
    #test
    def remove_provider(self):
        self.display_providers()
        found = False
        id = self.getProviderID()
        pName = self.getProviderName(id, 0)
        if pName != None:
            found = True
            path = os.getcwd() + '/Provider/' + pName
            shutil.rmtree(path)
        else:
            self.print_not_found()
        with open("Provider/ProviderList.json",mode="r") as file:
            data = json.load(file)
        for index,provider in enumerate(data['providers']):
            if provider['ProviderId'] == id:
                data['providers'].pop(index)
                found = True
        with open("Provider/ProviderList.json",mode="w") as file:
            json.dump(data,file, indent = 4)    
        return found
       #test
    def update_provider(self):
        id = self.getProviderID()
        pName = self.getProviderName(id, 0)
        if pName != None:
            found = True
            path = os.getcwd() + '/Provider/' + pName
            print("Path test: ", path)
        else:
            self.print_not_found()

    #Just a print statement to reuse in multiple functions
    def ask_for_ID(self):
        print("Please enter a valid provider ID number: ")
    
    def getProviderID(self):
        self.ask_for_ID()
        #print("\nPlease enter a valid provider ID number.")
        id = input("> ")

        if len(id) != 9 or id.isnumeric() == False:
            return self.getProviderID()
        else:
            return id
        
    def printWelcomeMessage(self, name):
        print("Welcome ", name)
        
    #test
    def getProviderName(self,id, choice):
        with open("Provider/ProviderList.json",mode="r") as file:
            data = json.load(file)
        for member in data['providers']:
            if member['ProviderId'] == id:
                name = member["ProviderName"]
                if choice == 1:
                    self.printWelcomeMessage(name)
                return name
        return None
    
    def add_comments(self):
        print("Would you like to enter comments about the service provided? [y/n]")
        ans2 = input("> ")
        if ans2 == 'y':
            print("Please enter a comment (100 characters): ")
            comment = input("> ")
            filename = f"{self.provider_name}.json"
            with open(filename, "w") as file:
                json.dump(comment, file)
    
    def load_validated(self,member_id,member_name):  
        s = Service()
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
                s.printServiceName(name)
                s.validateServiceName(member_id,date_service,name,self.provider_name,member_name,service_code)
                break
        if(validServiceCode == False):
            print("Invalid service code")
    
    #test 
    def load(self):
        self.provider_id = self.getProviderID()
        self.provider_name = self.getProviderName(self.provider_id, 1)
        while(self.provider_name == None):
            print("Invalid Provider Id")
            self.provider_id = self.getProviderID()
            self.provider_name = self.getProviderName(self.provider_id, 1)
        m = Member()
        m.member_id = m.getMemberID()
        m.member_name - m.getMemberName()
        var = m.validate_member(m.member_id)
        if var == True:
            if m.isSuspended(m.member_id) == True:
                m.printSuspended()
            else:
                print("Validated")
                self.load_validated(m.member_id)
        else:
            print("Invalid Number")
    
    def create_provider_weekly_report(self,date_service,member_id,member_name,service_code,service_fee):
        cwd = os.getcwd() #gets current working directory
        parent_dir = "Provider" #sets relative path in variable
        now = datetime.datetime.now()
            

        with open('Provider/ProviderList.json') as file:
            data = json.load(file)
        
        for provider in data['providers']:
            if provider['ProviderId'] == self.provider_id:
                pAddr = provider["ProviderAddr"]
                pCity = provider['ProviderCity']
                pState = provider['ProviderState']
                pZip = provider['ProviderZip']
        
        if os.path.exists(f"{cwd}/{parent_dir}/{self.provider_name}") == False:
            directory = f"{self.provider_name}/" #new member directory
            path = os.getcwd() + "/Provider/" + directory
            os.makedirs(path)
            

        dir_path = f"Member/{self.provider_name}"
        abs_path = os.path.abspath(dir_path)
        all_files = os.listdir(abs_path)
        all_files.sort(key=lambda x: os.path.getmtime(os.path.join(abs_path, x)), reverse=True)
        if len(all_files) != 0:
            latest_file = os.path.join(abs_path, all_files[0])

            latest_file_mtime = os.path.getmtime(latest_file)
            latest_file_datetime = datetime.datetime.fromtimestamp(latest_file_mtime)

            today = datetime.date.today()
            days_ago_7 = today - datetime.timedelta(days=7)
            directory = f"{self.provider_name}"
            path = os.getcwd() + "/Member/" + directory
            if latest_file_datetime.date() > days_ago_7:
                new_service = {
                    "Date_Of_Service": date_service,
                    "Date_received by computer": f"{now}",
                    "MemberName": member_name,
                    "MemberNum": member_id,
                    "ServiceCode": service_code,
                    "ServiceFee": service_fee
                }
                with open(f"{latest_file}","r") as file:
                    new_data = json.load(file)
                new_data['Services'].append(new_service)
                new_data['TotalConsultations'] += 1

                with open(f"{latest_file}","w") as file:
                    json.dump(new_data,file,indent=4)
            else:
            
                provider = {
                    "ProviderName": self.provider_name,
                    "ProviderID": self.provider_id,
                    "ProviderAddr": pAddr,
                    "ProviderCity": pCity,
                    "ProviderState": pState,
                    "ProviderZip": pCity,
                    "Services": [{
                        "Date_Of_Service": date_service,
                        "Date_received by computer": "",
                        "MemberName": member_name,
                        "MemberNum": member_id,
                        "ServiceCode": service_code,
                        "ServiceFee": service_fee
                    }],
                    "TotalConsultations": 1,
                    "TotalFee": "$0.00"
            }

                with open(f"{path}/{self.provider_name}_{date_service}.json",mode="w") as file:   #file 
                    json.dump(provider,file,indent= 4)
    
        else:
            
            
            with open(f"{dir_path}/{self.provider_name}_{date_service}.json",mode="w") as file:   #file 
                    json.dump(provider,file,indent= 4)

    def display_providers(self):
        with open('Provider/ProviderList.json') as f:
            data = json.load(f)

        # Extract fields
        rows = []
        for obj in data['providers']:
            rows.append([obj['ProviderName'], obj['ProviderId']])

        # Print table
        headers = ['Name', 'ID']
        print(tabulate(rows, headers=headers))