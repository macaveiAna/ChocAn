import json
import datetime
from datetime import date, timedelta
from time import strptime
import random
import os
from pathlib import Path
import shutil
import pandas as pd
from tabulate import tabulate

class Member:
 
    def __init__(self):
        self.member_id = ""
        self.member_name = ""
        self.strAddr = ""
        self.city = ""
        self.state = ""
        self.zip = ""
    
    def get_name(self):
        print("Please enter member's first name: ")
        first_name = input("> ")
        print("Please enter member's last name: ")
        last_name = input("> ")
        if first_name.isalpha() == False or last_name.isalpha() == False:
            print("Incorrect name format!")
            return self.get_name()
        else:
            member_name = first_name + " " + last_name
            return member_name

    def get_address(self):
        print("Please enter the Street Address: ")
        self.strAddr = input("> ")
        print("Please enter the City: ")
        self.city = input("> ")
        print("Please enter the State: ")
        self.state= input("> ")
        print("Please enter the zipcode: ")
        self.zip = input("> ")

        if self.city.isalpha() == False or self.state.isalpha() == False or self.zip.isnumeric() == False or len(self.state) != 2 or len(self.zip) != 5:
            print("Incorrect address format!")
            self.get_address()


    def enter_Member_details(self):
        self.member_name = self.get_name()
        for i in range(9):
            self.member_id += str(random.randint(0,9))
        self.get_address()
        self.add_member()

    def print_exists(self):
        print("Member already exists.") 

    def getMemberName(self,id):
        with open("Member/MemberDirectory.json",mode="r") as file:
            data = json.load(file)
        for member in data['members']:
            if member['MemberId'] == id:
                name = member["MemberName"]
                return name
        return None
    def print_not_found(self):
        print("Member does not exist.")
    def remove_member(self):
        found = False
        id = self.getMemberID()
        mName = self.getMemberName(id)
        if mName != None:
            found = True
            path = os.getcwd() + '/Member/' + mName
            shutil.rmtree(path)
        else:
            self.print_not_found()
        with open("Member/MemberDirectory.json",mode="r") as file:
            data = json.load(file)
        for index,member in enumerate(data['members']):
            if member['MemberId'] == id:
                found = True
                data['members'].pop(index)

        with open("Member/MemberDirectory.json",mode="w") as file:
            json.dump(data,file, indent = 4)    
        return found
    #first check in main function if member already exits
    def add_member(self):
        today = date.today()
        #print(today)
        
        member = {
                    "MemberName": self.member_name,
                    "MemberID": self.member_id,
                    "MemberAddr": self.strAddr,
                    "MemberCity": self.city,
                    "MemberState": self.state,
                    "MemberZip": self.zip,
                    "Services": [
                        
                    ],
            }
        
        cwd = os.getcwd() #gets current working directory
        parent_dir = "Member" #sets relative path in variable
        
        #If member already has a file, will print a statement that it exists
        if os.path.exists(f"{cwd}/{parent_dir}/{self.member_name}"): 
            self.print_exists()
        else:
            #creates the new member directory
            directory = f"{self.member_name}/" #new member directory
            '''
            p = Path(f"/ChocAn/Provider/{directory}") #sets path to the new provider's directory
            os.makedirs(p) #makes the directory
            '''
            path = os.getcwd() + "/Member/" + directory
            os.makedirs(path)
            
            with open(f"{path}/{self.member_name}_profile.json",mode="w") as file:   #file 
               json.dump(member,file,indent= 4)

            new_member = {
                "MemberName": self.member_name, 
                "MemberId": self.member_id, 
                #"MemberAddr": self.strAddr,
                #"MemberCity": self.city,
                #"MemberState": self.state,
                #"MemberZip": self.zip,
                "Status": "Active", 
                "last_payment": str(today)
                }
            
            
            #Appends the new member to the full member list
            with open(f"{cwd}/{parent_dir}/MemberDirectory.json",mode="r") as file:
                data = json.load(file)

            data["members"].append(new_member)
            with open(f"{cwd}/{parent_dir}/MemberDirectory.json",mode="w") as file:
                json.dump(data,file, indent = 4)
        
        options = {
                'Options': ['1. Add Another Member', '2. Return to Main Menu']
            }
        df = pd.DataFrame(options)
        df_styled = df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'left'})
        print(tabulate(df_styled.data, headers=df_styled.columns, tablefmt='fancy_grid', showindex=False))
        ch = int(input("Please enter your choice: "))
        if ch == 1:
            self.enter_Member_details()

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

    def getMemberID(self):
        print("\nPlease enter a valid member ID number.")
        id = input("> ")
        if len(id) != 9 or id.isnumeric() == False:
            return self.getMemberID()
        else:
            return id
    #function to read in user input
    def validate_member(self, member_id): # Checks if member exists 
        with open('Member/MemberDirectory.json') as file:
            data = json.load(file)
        
        for member in data['members']:
            if member['MemberId'] == member_id:
                return True
        
        return False

    def create_weekly_report(self,member_id,date_service,sName,pName):
        
        cwd = os.getcwd() #gets current working directory
        parent_dir = "Member" #sets relative path in variable
        
            

        with open('Member/MemberDirectory.json') as file:
            data = json.load(file)
        
        for member in data['members']:
            if member['MemberId'] == member_id:
                mName = member['MemberName']
                mAddr = member["MemberAddr"]
                mCity = member['MemberCity']
                mState = member['MemberState']
                mZip = member['MemberZip']
        
        if os.path.exists(f"{cwd}/{parent_dir}/{mName}") == False:
            directory = f"{mName}/" #new member directory
            path = os.getcwd() + "/Member/" + directory
            os.makedirs(path)
            

        dir_path = f"Member/{mName}"
        abs_path = os.path.abspath(dir_path)
        all_files = os.listdir(abs_path)
        all_files.sort(key=lambda x: os.path.getmtime(os.path.join(abs_path, x)), reverse=True)
        if len(all_files) != 0:
            latest_file = os.path.join(abs_path, all_files[0])

            latest_file_mtime = os.path.getmtime(latest_file)
            latest_file_datetime = datetime.datetime.fromtimestamp(latest_file_mtime)

            today = datetime.date.today()
            days_ago_7 = today - datetime.timedelta(days=7)
            directory = f"{mName}"
            path = os.getcwd() + "/Member/" + directory
            if latest_file_datetime.date() > days_ago_7:
                new_service = {
                    "Date_Of_Service": date_service,
                    "ProviderName": pName,
                    "ServiceName": sName
                }
                with open(f"{latest_file}","r") as file:
                    new_data = json.load(file)
                new_data['Services'].append(new_service)
                with open(f"{latest_file}","w") as file:
                    json.dump(new_data,file,indent=4)
            else:
            
                member = {
                    "MemberName": mName,
                    "MemberID": member_id,
                    "MemberAddr": mAddr,
                    "MemberCity": mCity,
                    "MemberState": mState,
                    "MemberZip": mZip,
                    "Services": [{
                        "Date_Of_Service": date_service,
                        "ProviderName": pName,
                        "ServiceName": sName
                    }],
                }

                with open(f"{path}/{mName}_{date_service}.json",mode="w") as file:   #file 
                    json.dump(member,file,indent= 4)
    
        else:
            member = {
                    "MemberName": mName,
                    "MemberID": member_id,
                    "MemberAddr": mAddr,
                    "MemberCity": mCity,
                    "MemberState": mState,
                    "MemberZip": mZip,
                    "Services": [{
                        "Date_Of_Service": date_service,
                        "ProviderName": pName,
                        "ServiceName": sName
                    }],
            }
            with open(f"{dir_path}/{mName}_{date_service}.json",mode="w") as file:   #file 
                    json.dump(member,file,indent= 4)
    def display_members(self):
        with open('Member/MemberDirectory.json') as f:
            data = json.load(f)

        # Extract fields
        rows = []
        for obj in data['members']:
            rows.append([obj['MemberName'], obj['MemberId']])

        # Print table
        headers = ['Name', 'ID']
        print(tabulate(rows, headers=headers))
