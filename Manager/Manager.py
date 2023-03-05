from Provider import *
from Member import *
from Service import *
from tabulate import tabulate
import pandas as pd
#generate different reports for provider and member
#able to add member,delete member, same with provider and able to also do the same with services  
class Manager:
    def __init__(self):
        pass
    '''
    def getOption(self):
        option = int(input("> "))
        if (option < 0 or option > 4):
            print("Please enter a valid option!")
            self.getOption()
        return option
    '''
    def displayMenu(self):
        options = {
            'Services': ['1. Generate reports', '2. Modify Members', '3. Modify Providers', '4. Modify Services', '5. Quit']
        }
        df = pd.DataFrame(options)
        df_styled = df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'left'})
        print(tabulate(df_styled.data, headers=df_styled.columns, tablefmt='fancy_grid', showindex=False))
        return int(input("Please enter your choice: "))
    
    def menu(self):
        print("Welcome back!")
        while True:
            option = self.displayMenu()
            match option:
                case 1:
                    print("Which report do you want to generate?")
                    print("1.Member report")
                    #Need to do one member and all members
                    print("2.Provider report")
                    #Need to do one provider & all providers
                    print("3.EFT Report")
                    print("4.Summary Report")
                case 2:
                    m = Member()
                
                    while True:
                        print("What do you want to do?")
                        print("1. Add member")
                        print("2. Remove member")
                        print("3. Update member records")
                        print("Please choose an option..")
                        response = int(input("> "))
                        if response == 1:
                            m.enter_Member_details()
                        elif response == 2:
                            m.remove_member()
                        elif response == 3:
                            #m.update_provider_records()
                            pass
                        else:
                            print("Enter a valid option!")
                            continue  # repeat the loop until a valid option is entered
                        break  # exit the loop once a valid option is selected     


                case 3:
                    p = Provider()
                    while True:
                        print("What do you want to do?")
                        print("1. Add provider")
                        print("2. Remove provider")
                        print("3. Update provider records")
                        print("Please choose an option..")
                        response = int(input("> "))
                        if response == 1:
                            p.enter_Provider_details()
                        elif response == 2:
                            p.remove_provider()
                        elif response == 3:
                            p.update_provider_records()
                        else:
                            print("Enter a valid option!")
                        continue  # repeat the loop until a valid option is entered
                        break  # exit the loop once a valid option is selected         
                case 4:
                    #s = Service()
                    while True:
                        print("What do you want to do?")
                        print("1.Add service")
                        print("2.Remove service")
                        print("3.Update services")
                        print("Please choose an option..")
                        response = int(input("> "))
                        if response == 1:
                            p.enter_Provider_details()
                        elif response == 2:
                            p.remove_provider()
                        elif response == 3:
                            p.update_provider_records()
                        else:
                            print("Enter a valid option!")
                            continue  # repeat the loop until a valid option is entered
                        break  # exit the loop once a valid option is selected 
                case 5:
                    print("SEE YOU AGAIN TOMORROW!")    
            if not option!=5:
                break;
     

    def load(self):
        self.menu()
    