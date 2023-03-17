
from Provider import Provider
from Manager import *
import pandas as pd
from tabulate import tabulate
import os


class Terminal:
    def __init__(self):
        self.type = ""
        
    #test
    def getInitInput(self):
        options = {
                'WELCOME TO CHOCAN': ['Options','1. If you are a Provider', '2. If you are a Manager', '3. Quit']
            }
        df = pd.DataFrame(options)
        df_styled = df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'left'})
        print(tabulate(df_styled.data, headers=df_styled.columns, tablefmt='fancy_grid', showindex=False))
        choice = input("Please enter your choice: ")
        if choice.isnumeric() == False or (int(choice) != 1 and int(choice) != 2 and int(choice) != 3):
            if os.name == 'nt':  # For Windows
                os.system('cls')
            else:  # For Linux/Mac
                os.system('clear')
            print("Invalid Input! Try again:")
            return self.getInitInput()
        else:        
            return int(choice)
    
    def setType(self, choice):
        if choice == 1:
            self.type = "Provider"
        elif choice == 2:
            self.type = "Manager"
        else:
            self.type = None
        return self.type
        
    #test  
    def loadTerminal(self):
        choice = self.getInitInput()
        while choice != 3:
            self.setType(choice)
            
            if os.name == 'nt':  # For Windows
                os.system('cls')
            else:  # For Linux/Mac
                os.system('clear')

            if self.type == "Provider": # if type is provider
                provider = Provider()
                provider.load()
            
            else: # if type is manager
                manager = Manager()
                manager.load()
               
            choice = self.getInitInput()
        