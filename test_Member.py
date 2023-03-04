import pytest
import Member
import json
import os
import datetime

obj1 = Member.Member()
#when testing, please run with pytest -s to test output
def test_enter_Provider_details():
    obj1.enter_Provider_details()
    
    #check if it's not empty
    assert obj1.member_name != ""
    assert obj1.member_name != None
    assert len(obj1.member_name) <= 25
    assert obj1.member_id != ""
    assert obj1.member_id != None
    assert len(obj1.member_id) == 9
    '''
    assert obj1.strAddr != ""
    assert obj1.strAddr != None
    assert len(obj1.strAddr) <= 25
    assert obj1.city != ""
    assert obj1.city != None
    assert len(obj1.city) <= 14
    assert obj1.state != ""
    assert obj1.state != None
    assert len(obj1.state) == 2
    assert obj1.zip != ""
    assert obj1.zip != None
    assert len(obj1.zip) == 5
    '''


def test_add_member():
    #obj1.add_member('80192104', 'T_' + datetime.datetime.now())

    with open("Member/MemberDirectory.json", "r") as file:
        expected = json.load(file)
    new_member = {
        "MemberName": 'T_' + datetime.datetime.now(), 
        "MemberId": '80192104', 
        "Status": "Active", 
        "last_payment": str(today)
        }
    expected["members"].append(new_member)

    obj1.add_member('80192104', 'T_' + datetime.datetime.now())

    with open("Member/MemberDirectory.json", "r") as file:
        whatWeHave = json.load(file)

    assert expected == whatWeHave


def test_isSuspended():
    pass

def test_getMemberID():
    id = obj1.getMemberID()
    assert len(id) == 9
    assert id.isnumeric() == True
    assert id != '000000000'

def validate_member():
    pass