import pytest
from ChocAn import Terminal



#Unit Test file for ChocAn functions
 
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


