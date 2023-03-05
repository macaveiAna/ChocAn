import json
import datetime
from datetime import date, timedelta
from time import strptime
import os
from pathlib import Path

class Member:
 
    def __init__(self):
        self.member_id = ""
        self.member_name = ""
        self.strAddr = ""
        self.city = ""
        self.state = ""
        self.zip = ""
    

    #first check in main function if member already exits
    def add_member(self):
        today = date.today()
        #print(today)
        new_member = {
            "MemberName": self.member_name, 
            "MemberId": self.member_id, 
            "Status": "Active", 
            "last_payment": str(today)
            }
        
        data["members"].append(new_member)
        cwd = os.getcwd() #gets current working directory
        parent_dir = "Member/" #sets relative path in variable
        
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

            #Appends the new member to the full member list
        with open(f"{cwd}/{parent_dir}/MemberDirectory.json",mode="r") as file:
            data = json.load(file)
  
        with open(f"{cwd}/{parent_dir}/MemberDirectory.json",mode="w") as file:
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
    
    def pay_monthly_fee(self):
        pass
        
    #def remove_member(self):
        #pass
   
