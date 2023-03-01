# Developers Ana, Pooja, Melissa, Emma, Mahad
# CS314 Group 2
#

#import ChocAn as object
from ChocAn import *
from LLL import *
def main():
    # Creates var 'terminal' to hold Terminal object
    terminal = Terminal()
    member = Member()
    list = LLL()

    print("Here are the existing members: \n")
    list.load()
    list.display()
    
    terminal.loadTerminal()
    member.add_member("1234", "hi")
    


if __name__ == "__main__":
    main()