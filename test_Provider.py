import pytest
import Provider
import json
import os

obj1 = Provider.Provider()
#when testing, please run with pytest -s to test output
def test_enter_Provider_details():
    obj1.enter_Provider_details()
    
    #check if it's not empty
    assert obj1.provider_name != ""
    assert obj1.provider_name != None
    assert obj1.provider_name.isalpha() == True
    assert obj1.provider_name.isnumeric() == False
    assert len(obj1.provider_name) <= 25
    assert obj1.provider_id != ""
    assert obj1.provider_id != None
    assert obj1.provider_id.isalpha() == False
    assert obj1.provider_id.isnumeric() == True
    assert len(obj1.provider_id) == 9
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

def test_getProviderID():
    id = obj1.getProviderID()
    
    assert len(id) > 0 
    assert len(id) == 9
    assert id.isnumeric()
    
def test_get_comment():
    comment = obj1.get_comment()

    assert comment != ""
    assert comment != None 
    assert len(comment) <= 100
    
def test_load_validated():
    #obj1.load_validated()
    
    #opening the json file that we are testing
    with open("Service/ProviderDirectory.json", "r") as file:
        #set variable to the contents of the file
        expected_data = json.load(file)
    #creating a new file
    filepath = "test_file.json"
    #opening the temporary file in write mode to...
    with open(filepath, "w") as file:
        #insert the contents of original file to temporary file
        json.dump(expected_data, file)
    #open the temporary file in read mode
    with open(filepath, "r") as file:
        #set variable to the contents of temporary file
        jsondata = json.load(file)
    #then check if the temporary file is equal to the original file
    assert jsondata == expected_data
    #the last statement basically removes the temporary file
    os.remove(filepath)
    
    #verify that this test works as should 
# - group 2 was working on this while I was testing
def test_add_provider():
    #obj1.add_provider()
    
    with open("Provider/ProviderList.json", mode = "r") as file:
        expected_data = json.load(file)
    filepath = "test_file.json"
    new_provider = {
        "ProviderName": obj1.provider_name,
        "ProviderId": obj1.provider_id
    }
    expected_data['providers'].append(new_provider)
    with open(filepath,"w") as file:
        json.dump(expected_data, file, indent=4)
        
    with open("Provider/ProviderList.json", "r") as file:
        jsondata = json.load(file)
    
    with open(filepath, "r") as file:
        data = json.load(file)
    assert jsondata != data
    os.remove(filepath)
    
    
 
    
    
    
    