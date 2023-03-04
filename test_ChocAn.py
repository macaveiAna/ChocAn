import pytest
from ChocAn import Terminal
import Provider


#Unit Test file for ChocAn functions
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
    
#Test the type for the terminal
# Need to figure out how to do in one test
def test_setType(setup: Terminal):
    setup = Terminal()
    setup.setType(1)
    assert setup.type == "Provider"

def test_setType2(setup: Terminal):
    setup = Terminal()
    setup.setType(2)
    assert setup.type =="Manager"



#def loadTerminal
#def test_loadTerminal():

# Test input/output resource:
# https://gist.github.com/mauricioaniche/671fb553a81df9e6b29434b7e6e53491

test_input = []
test_output = []

def mock_input(s):
    test_output.append(s)
    return test_input.pop(0)

def mock_input_output():
    global test_input, test_output

    test_input = []
    test_output = []

def disp_output():
    global test_output
    return test_output

def set_input(some_input):
    global test_input

    mock_input_output()
    test_input = some_input
#getInitInput Test
#def test_getInitInput(setup):
    #input = 1

    #choice = terminal.getInitInput()