
from Provider import Provider
from Manager import *
import pandas as pd
from tabulate import tabulate


class Terminal:
    def __init__(self):
        self.type = ""
        
    #test
    def getInitInput(self):
        options = {
                'WELCOME TO CHOCAN': ['Options','1. If you are a Provider', '2. If you are a Manager']
            }
        df = pd.DataFrame(options)
        df_styled = df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'left'})
        print(tabulate(df_styled.data, headers=df_styled.columns, tablefmt='fancy_grid', showindex=False))
        choice = int(input("Please enter your choice: "))
        return choice
    
    def setType(self, choice):
        if choice == 1:
            self.type = "Provider"
        else:
            self.type = "Manager"

        return self.type
        
    #test  
    def loadTerminal(self):
        choice = self.getInitInput()
        self.setType(choice)

        if self.type == "Provider": # if type is provider
            provider = Provider()
            provider.load()
            
        else: # if type is manager
            manager = Manager()
            manager.load()