import pytest
import Provider

obj1 = Provider.Provider()
#when testing, please run with pytest -s to test output
def test_enter_Provider_details():
    obj1.enter_Provider_details()
    
    #check if it's not empty
    assert obj1.provider_name != ""
    assert obj1.provider_name != None
    assert obj1.provider_id != ""
    assert obj1.provider_id != None
    assert obj1.strAddr != ""
    assert obj1.strAddr != None
    assert obj1.city != ""
    assert obj1.city != None
    assert obj1.state != ""
    assert obj1.state != None
    assert obj1.zip != ""
    assert obj1.zip != None