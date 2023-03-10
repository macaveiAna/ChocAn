import json
from Member import *
from Service import *
import random
import os
from pathlib import Path
import shutil
import pandas as pd
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

        cwd = os.getcwd() #gets current working directory
        parent_dir = "Provider" #sets relative path in variable
        
        #If provider already has a file, will print a statement that it exists
        if os.path.exists(f"{cwd}/{parent_dir}/{self.provider_name}"): 
            self.print_exists()

        else:
            #Creates the new provider directory
            directory = f"{self.provider_name}/" #new provider directory
            path = os.getcwd() + "/Provider/" + directory  #sets path to the new provider's directory
            os.makedirs(path)
            #Contents for file that is uploaded
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
            #with open(f"{path}/{self.provider_name}_{str(today)}.json",mode="w") as file:   #file 
             #  json.dump(provider,file,indent= 4)
            with open(f"{path}/{self.provider_name}_profile.json",mode="w") as file:   #file  
               json.dump(provider,file,indent= 4)

            #Opens the path to the Provider folder for the
            # list of providers in the json file
            
            with open(f"{cwd}/{parent_dir}/ProviderList.json",mode="r") as file:
                data = json.load(file)
                
            #New provider data for the json file containing all providers in Provider folder
            new_provider = {
                "ProviderName": self.provider_name,
                "ProviderId": self.provider_id,
                #"ProviderAddr": self.strAddr, # I don't think these are needed in the full list
                #"ProviderCity": self.city,
               # "ProviderState": self.state,
                #"ProviderZip": self.zip,
            }
            #Appends the new provider to the full provider list
            data['providers'].append(new_provider)
            with open(f"{cwd}/{parent_dir}/ProviderList.json",mode="w") as file:
                json.dump(data,file,indent=4)

        options = {
                'Options': ['1. Add Another Provider', '2. Return to Main Menu']
            }
        df = pd.DataFrame(options)
        df_styled = df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'left'})
        print(tabulate(df_styled.data, headers=df_styled.columns, tablefmt='fancy_grid', showindex=False))
        ch = int(input("Please enter your choice: "))
        if ch == 1:
            self.load()
            
            
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
    
    def update_Pmenu(self):
        print("To update name, enter 1")
        print("To update address, enter 2")
        choice = input()
        return choice

    #Get updated name
    def ask_name(self):
        print("Write the updated name of the provider: ")
        new_pName = input()
        return new_pName
  
    
    #Update the Provider profile & info in ProviderList
    def update_provider(self):
        id = self.getProviderID()
        pName = self.getProviderName(id, 0)
        if pName == None:
                return
        choice = self.update_Pmenu()
        print("choice ", choice)
        if choice == "1": #Update Provider Name
            path = os.getcwd() + '/Provider/' + pName #Go to the dir
            #print("Path test: ", path)
            self.provider_name = new_name = self.ask_name()    # Need edit function to call
            new_path = os.getcwd() + '/Provider/' + new_name
            os.rename(f"{path}/{pName}.json", f"{path}/{new_name}.json") #Renaming Profile
            shutil.move(path, new_path) #Move the dir & contents to new_named dir
    
            #Need to edit the dictionary now
           # with open(f"{new_path}/{new_name}.json",mode="w") as file:   #file 
            #   json.dump(provider,file,indent= 4)
                #data = json.load(file)
            
        """
            if pName in data:
                    del data[pName]
                    cacheDict = dict(data)
                    cacheDict.update({pName:new_name})
                    with open(f"{new_path}/{new_name}.json",mode="w") as file:
                    # Dump cached dict to json file
                        json.dump(cacheDict, file, indent=4)
                      
            
            #shutil.move(f"{new_path}/{pName}.json", f"{new_path}/{new_name}.json")
               
            #Update the ProviderList JSON
            with open("Provider/ProviderList.json",mode="r") as file:
                data = json.load(file)
            for index,provider in enumerate(data['providers']):
                if provider['ProviderId'] == id:
                 #data['providers'].pop(index)
                 found = True
            with open("Provider/ProviderList.json",mode="w") as file:
                json.dump(data,file, indent = 4)    
        else:
            self.print_not_found()
        """


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
    
    def get_comment(self):
        print("Please enter a comment (100 characters): ")
        comment = input('> ')
        if len(comment) > 100:
            print('Your comment surpassed 100 characters.\nPlease Redo!')
            return self.get_comment()
        else:
            return comment

    def add_comments(self, provider_name):
        print("Would you like to enter comments about the service provided? [y/n]")
        ans2 = input("> ")
        if ans2 == 'y':
            comment = self.get_comment()
            filename = f"{provider_name}.json"
            with open(filename, "w") as file:
                json.dump(comment, file)
    
    def load_validated(self, provider_name, date_of_service, member_name):  
        s = Service()
        #print("Please enter the date the service was provided:")
        #date_service = input("> ")
        print("Please enter service code:")
        service_code = input("> ")
        validServiceCode = False
        with open("Service/ProviderDirectory.json") as file:
            data = json.load(file)
        for service in data['services']:
            if service['serviceCode'] == service_code:
                sname = service['serviceName']
                validServiceCode = True
                s.printServiceName(sname)
                s.validateServiceName(sname, provider_name, member_name, date_of_service)
                break
        if(validServiceCode == False):
            print("Invalid service code")
            self.load_validated(provider_name, date_of_service, member_name)
            
    def get_date_service(self, provider_name, member_name):
        print("\nPlease enter the date the service was provided. ")
        year = int(input('Enter year (yyyy): '))
        month = int(input('Enter month (mm): '))
        day = int(input('Enter day (dd): '))

        d = date(year, month, day)
      
        if date.today() < d:
            print("Invalid Date!")
            self.get_date_service(provider_name, member_name)
        elif date.today() - timedelta(days=6) > d:
            print("Invalid Date!")
            self.get_date_service(provider_name, member_name)
        else:
            self.load_validated(provider_name, d, member_name)
        
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
        m.member_name = m.getMemberName(m.member_id)
        while(m.member_name == None):
            print("Invalid Member Id")
            m.member_id = m.getMemberID()
            m.member_name = m.getMemberName(m.member_id)
        var = m.validate_member(m.member_id)
        if var == True:
            if m.isSuspended(m.member_id) == True:
                m.printSuspended()
            else:
                print("Validated")
                self.get_date_service(self.provider_name, m.member_name)
        

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