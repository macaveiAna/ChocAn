import pytest
import Service
import json
import os

obj1 = Service.Service()

def test_enter_service_details():
    obj1.enter_service_details()
    
    assert obj1.service_name != ""
    assert obj1.service_name != None
    assert len(obj1.service_name) <= 20
    
    #do NOT insert a dollar sign ($)
    assert obj1.service_fee != ""
    assert obj1.service_fee != None

#after testing this function check in ProviderDirectory.json
#to verify success
def test_add_service():
    data = obj1.load_file()
    test_file = "Test.json"
    new_service = {
        "serviceName": obj1.service_name,
        "serviceCode": obj1.service_code,
        "servicePrice": "$" + obj1.service_fee
    }
    data['services'].append(new_service)
    with open(test_file, "w") as file:
        json.dump(data, file, indent=4)
    
    data2 = obj1.load_file()
    with open("Test.json", "r") as file:
        data3 = json.load(file)
    
    assert data2 != data3
    os.remove(test_file)
    

def test_getServiceCode():
    code = obj1.getServiceCode()
    
    assert code != ""
    assert code != None 
    assert len(code) == 6
    assert code.isnumeric() == True
    assert code.isalpha() == False
    
    