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
    assert len(obj1.provider_name) <= 25
    assert obj1.provider_id != ""
    assert obj1.provider_id != None
    assert len(obj1.provider_id) == 9
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
    
#def test_add_provider():

#def test_remove_provider():

def test_getProviderID():
    id = obj1.getProviderID()
    
    assert len(id) > 0 
    assert len(id) <= 9
    assert id.isnumeric()
    
def test_load_validated():
    obj1.load_validated()
    
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
    
        