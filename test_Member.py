import pytest
import Member
import json
import os
import datetime

obj1 = Member.Member()
#when testing, please run with pytest -s to test output

#Please test with id that exists in MemberDirectory.json   
def test_getMemberID():
    id = obj1.getMemberID()
    assert len(id) == 9
    assert len(id) > 0
    assert id.isnumeric()
    assert id != '000000000'
 
def test_get_address():
    obj1.get_address()
    
    assert obj1.strAddr != ""
    assert obj1.strAddr != None
    assert len(obj1.strAddr) <= 25
    assert obj1.city != ""
    assert obj1.city != None
    assert obj1.city.isalpha() == True
    assert obj1.city.isnumeric() == False
    assert len(obj1.city) <= 14
    assert obj1.state != ""
    assert obj1.state != None
    assert obj1.state.isalpha() == True
    assert obj1.state.isnumeric() == False
    assert len(obj1.state) == 2
    assert obj1.zip != ""
    assert obj1.zip != None
    assert obj1.zip.isalpha() == False
    assert obj1.zip.isnumeric() == True
    assert len(obj1.zip) == 5

def test_get_name():
    name = obj1.get_name()
   #check if it's not empty
    assert name != ""
    assert name != None
    #assert name.isalpha() == True
    assert name.isnumeric() == False
    assert len(name) <= 25  

 
    
def test_add_member():
    today = datetime.date.today()
    with open("Member/MemberDirectory.json", "r") as file:
        expected_data = json.load(file)
    filepath = "test_file.json"
    with open("test_file.json", "w") as file:
        json.dump(expected_data, file, indent=4)
    new_member = {
        "MemberName": 'T_', 
        "MemberId": '80192104', 
        "Status": "Active", 
        "last_payment": str(today) #work on this part
        }
    expected_data["members"].append(new_member)

    #obj1.add_member('80192104', 'T_' + datetime.datetime.now())

    with open("test_file.json", "w") as file:
        json.dump(expected_data, file, indent=4)
        
    with open("Member/MemberDirectory.json", "r") as file:
        jsondata = json.load(file)
        
    with open("test_file.json", "r") as file:
        test_data = json.load(file)

    assert jsondata != test_data
    os.remove(filepath)
'''


'''
def test_remove_member():
    id = obj1.getMemberID()
    #name = obj1.getMemberName(id)
    #open the file 
    with open("Member/MemberDirectory.json", "r") as file:
        original_data = json.load(file)
    filepath = "test_file.json"
    #pop off the member
    for index, member in enumerate(original_data['members']):
        if member['MemberId'] == id:
            original_data['members'].pop(index)
    #open in write mode
    with open("test_file.json", mode = "w") as file:
        json.dump(original_data, file, indent = 4)
    #then dump the updated file
    with open("Member/MemberDirectory.json", "r") as file:
        new_data = json.load(file)
        
    with open("test_file.json", "r") as file:
        jsondata = json.load(file)
    
    assert jsondata != new_data
    
    os.remove(filepath)
    
    
        

