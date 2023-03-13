import pytest
import Member
import json
import os
import datetime

obj1 = Member.Member()
#when testing, please run with pytest -s to test output
def test_enter_Member_details():
    obj1.enter_Member_details()
    
    #check if it's not empty
    assert obj1.member_name != ""
    assert obj1.member_name != None
    assert obj1.member_name.isalpha == True
    assert obj1.member_name.isnumeric == False
    assert len(obj1.member_name) <= 25
    assert obj1.member_id != ""
    assert obj1.member_id != None
    assert obj1.member_id.isalpha == False
    assert obj1.member_id.isnumeric == True
    assert len(obj1.member_id) == 9
 
def test_get_address():
    obj1.get_address()
    
    assert obj1.strAddr != ""
    assert obj1.strAddr != None
    assert len(obj1.strAddr) <= 25
    assert obj1.city != ""
    assert obj1.city != None
    assert obj1.city.isalpha == True
    assert obj1.city.isnumeric == False
    assert len(obj1.city) <= 14
    assert obj1.state != ""
    assert obj1.state != None
    assert obj1.state.isalpha == True
    assert obj1.state.isnumeric == False
    assert len(obj1.state) == 2
    assert obj1.zip != ""
    assert obj1.zip != None
    assert obj1.zip.isalpha == False
    assert obj1.zip.isnumeric == True
    assert len(obj1.zip) == 5
    
    
    
def test_add_member():
    #obj1.add_member('80192104', 'T_' + datetime.datetime.now())
    today = datetime.date.today()
    with open("Member/MemberDirectory.json", "r") as file:
        expected_data = json.load(file)
    filepath = "test_file.json"
    new_member = {
        "MemberName": 'T_' + datetime.datetime.now(), 
        "MemberId": '80192104', 
        "Status": "Active", 
        "last_payment": str(today) #work on this part
        }
    expected_data["members"].append(new_member)

    obj1.add_member('80192104', 'T_' + datetime.datetime.now())

    with open("Member/MemberDirectory.json", "w") as file:
        json.dump(expected_data, file)
        
    with open("Member/MemberDirectory.json", "r") as file:
        jsondata = json.load(file)

    assert expected_data == jsondata
    os.remove(filepath)


def test_isSuspended():
    pass

def test_getMemberID():
    id = obj1.getMemberID()
    assert len(id) == 9
    assert id.isnumeric() == True
    assert id != '000000000'

def validate_member():
    pass