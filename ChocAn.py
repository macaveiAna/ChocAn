import json
from datetime import date

#generate different reports for provider and member
#manager is able to suspend a member if they have not yet paid 
#their monthly fees    
class Manager:
    def __init__(self):
        pass
    
    def check_member_status(self):
        pass

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

    def setIfSuspended(self, member_id):
        #today = date.today() + timedelta(days=30)

        with open("Member/MemberDirectory.json", "r") as file:
            data = json.load(file)
        
        for member in data['members']:
            if member['MemberId'] == member_id:
                date = strptime(member["last_payment"], "%Y/%m/%d")
                date = date + timedelta(days=30)

                if date.today() > date:
                    # suspend this account
                    member['Status'] = 'Suspended'
                    self.printSuspended()
                    return False
                else:
                    return True

        return False # default return. If trouble finding account
        

    
    #function to read in user input
    def validate_member(self, member_id):
        with open('Member/MemberDirectory.json') as file:
            data = json.load(file)
        
        for member in data['members']:
            if member['MemberId'] == member_id:
                status = member['Status']
                if status == 'Active':
                    return self.setIfSuspended(member_id)
                elif status == 'Suspended':
                    return False
        
        return False
    
    def pay_monthly_fee(self):
        pass
        
    #def remove_member(self):
        #pass
        
        
        
    #function to compare what is in the file


class Provider:
    def __init__(self):
        self.provider_id = ""
        self.provider_name = ""
    
    def getProviderID(self):
        print("\nPlease enter a valid provider ID number.")
        id = input("> ")

        if len(id) != 9 or id.isnumeric() == False:
            return self.getProviderID()
        else:
            return id

    def getProviderName(self,id):
        with open("Provider/ProviderList.json",mode="r") as file:
            for line in file:
                parts = line.strip().split(":")
                if parts[0] == id:
                    return parts[1]

    def getMemberID(self):
        print("\nPlease enter a valid member ID number.")
        id = input("> ")
        if len(id) != 9 or id.isnumeric() == False:
            return self.getMemberID()
        else:
            return id

    def load(self):
        self.provider_id = self.getProviderID()
        self.provider_name = self.getProviderName(self.provider_id)
        print("Welcome ", self.provider_name)
        m = Member()
        m.member_id = self.getMemberID()
        #got member contents to print from json file
        #now we need to figure out how to check the status and
        #charge the member depending if they are suspended or not
        
        var = m.validate_member(m.member_id)
        
        if var == True:
            print("Validated")
            # call function that does rest of work: self.load_validated()
        else:
            print("Invalid Number")
            


'''
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
        
     

    
    #function to read in user input
    def validate_member(self, member_id):
        with open('Member/MemberDirectory.json') as file:
            
            for line in file:
                parts = line.strip().split(" ")
                if parts[0] == member_id:
                    return True
            
            data = json.load(file)
        
        for member in data['members']:
            if member['MemberId'] == member_id:
                status = member['Status']
                if status == 'Suspended':
                    return False

                
        
        
        #return False
    
    def pay_monthly_fee(self):
        pass
        
    #def remove_member(self):
        #pass
        
        
        
    #function to compare what is in the file
'''



class Services:
    pass


class Terminal:
    def __init__(self):
        self.type = ""
    
    def getInitInput(self):
        choice = int(input("> "))
        if choice != 1 and choice != 2:
            print("Please enter valid choice.")
            self.getInitInput()
        
        return choice

    def setType(self, choice):
        if choice == 1:
            self.type = "Provider"
        else:
            self.type = "Manager"

        return self.type
        
    def getMemberID(self):
        print("\nPlease enter a valid member ID number.")
        id = input("> ")
        if len(id) != 9 or id.isnumeric() == False:
            return self.getMemberID()
        else:
            return id
        
    def loadTerminal(self):
        print("\n\nWelcome to ChocAn!\n")
        print("Enter 1 if you are a Provider.")
        print("Enter 2 if you are a Manager.")

        choice = self.getInitInput()
        self.setType(choice)

        if self.type == "Provider": # if type is provider
            provider = Provider()
            provider.load()
            
        else: # if type is manager
            manager = Manager()
            manager.load()