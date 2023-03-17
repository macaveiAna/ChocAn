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
        self.member_name = None
        self.strAddr = ""
        self.city = ""
        self.state = ""
        self.zip = ""
    
    #getting the user to enter the name
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
        while not self.city.isalpha():
            print("Not a valid city, try again.")
            self.city = input("Please enter a valid city: ")
        print("Please enter the State: ")
        self.state = input("> ")
        while len(self.state) != 2 or (not self.state.isalpha()):
            print("Not a valid state, try again.")
            self.state = input("Please enter a valid state: ")
        print("Please enter the zipcode: ")
        self.zip = input("> ")
        while len(self.zip) != 5 or (not self.zip.isdigit()):
            print("Not a 5 digit number, try again.")
            self.zip = input("Please enter your 5 digit zipcode: ")

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

    #going inside the member directory to get the name
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
            path = os.getcwd() + "/Member/" + directory
            os.makedirs(path)
            
            with open(f"{path}/{self.member_name}_profile.json",mode="w") as file:   #file 
               json.dump(member,file,indent= 4)

            new_member = {
                "MemberName": self.member_name, 
                "MemberId": self.member_id, 
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

    def update_Mmenu(self):
        options = {
                'Options': ['1. Update Name', '2. Update Address']
            }
        df = pd.DataFrame(options)
        df_styled = df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'left'})
        print(tabulate(df_styled.data, headers=df_styled.columns, tablefmt='fancy_grid', showindex=False))
        choice = input("Please enter your choice: ")
        
        return choice

    #Get updated name
    def ask_name(self):
        print("Write the updated name of the Member: ")
        new_mName = input()
        return new_mName
    
    def update_member(self):
        id = self.getMemberID()
        mName = self.getMemberName(id)
        if mName == None:
                return
        choice = self.update_Mmenu()
        path = os.getcwd() + '/Member/' + mName #Go to the dir
        if(os.path.exists(path)):
            if choice == "1": #Update Memeber Name
            #path = os.getcwd() + '/Provider/' + pName #Go to the dir
                #if(os.path.exists(path)):
                    new_name = self.ask_name()    # Need edit function to call
                    new_path = os.getcwd() + '/Member/' + new_name
                    os.rename(f"{path}/{mName}_profile.json", f"{path}/{new_name}_profile.json") #Renaming Profile
                    shutil.move(path, new_path) #Move the dir & contents to new_named dir

                    #Need to edit the dictionary now
                    with open(f"{new_path}/{new_name}_profile.json",mode="r") as file:   #file 
                        data = json.load(file)
                    data["MemberName"] = new_name
                    with open(f"{new_path}/{new_name}_profile.json",mode="w") as file:   #file 
                        json.dump(data,file,indent=4)
                    with open("Member/MemberDirectory.json",mode="r") as file:   #file 
                        data = json.load(file)
    
                    for provider in data["members"]:
                        if provider["MemberName"] == mName:
                            provider["MemberName"] = new_name
                    with open("Member/MemberDirectory.json",mode="w") as file:
                            json.dump(data,file,indent=4)
            
            elif choice == "2": #Update Provider Address
                print("Please enter the updated Street Address: ")
                new_StrAdd = input("> ")
                print("Please enter the updated City: ")
                new_city = input("> ")
                print("Please enter the updated State: ")
                new_state= input("> ")
                print("Please enter the updated zipcode: ")
                new_zip = input("> ")
                with open(f"{path}/{mName}_profile.json",mode="r") as file:   #file 
                        data = json.load(file)
                data["MemberAddr"] = new_StrAdd
                data["MemberCity"] = new_city
                data["MemberState"] = new_state
                data["MemberZip"] = new_zip
                with open(f"{path}/{mName}_profile.json",mode="w") as file:   #file 
                        json.dump(data,file,indent=4)

            else:
                print("Invalid option!")
                self.update_member()
        else:
            self.print_not_found()


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
