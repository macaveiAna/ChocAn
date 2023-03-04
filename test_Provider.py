import pytest
import Provider

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
    obj1.getProviderID()
    
    assert len(obj1.getProviderID()) > 0 
    assert len(obj1.getProviderID()) <= 9
    assert obj1.getProviderID().isnumeric()
    