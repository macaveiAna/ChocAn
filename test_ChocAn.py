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



#def loadTerminal
#def test_loadTerminal():

# Test input/output resource:
# https://gist.github.com/mauricioaniche/671fb553a81df9e6b29434b7e6e53491
