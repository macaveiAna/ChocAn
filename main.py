# Developers Ana, Pooja, Melissa, Emma, Mahad
# CS314 Group 2
#

from ChocAn import *
import os

def main():
    # Creates var 'terminal' to hold Terminal object
    terminal = Terminal()
    terminal.loadTerminal()

if __name__ == "__main__":
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/Mac
        os.system('clear')
    main()