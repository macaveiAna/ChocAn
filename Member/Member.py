import json
import datetime
from datetime import date, timedelta
from time import strptime

class Member:
 
    def __init__(self):
        self.member_id = ""
        self.member_name = ""
     
   
    #first check in main function if member already exits
    def add_member(self, member_id, member_name):
        today = date.today()
        #print(today)
       
        with open("Member/MemberDirectory.json", "r") as file:
            data = json.load(file)
        new_member = {
            "MemberName": member_name, 
            "MemberId": member_id, 
            "Status": "Active", 
            "last_payment": str(today)
            }
        data["members"].append(new_member)
        with open("Member/MemberDirectory.json", "w") as file:
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
        