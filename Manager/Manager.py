from Provider import *
from Member import *
from Service import *
from tabulate import tabulate
import pandas as pd

#generate different reports for provider and member
#able to add member,delete member, same with provider and able to also do the same with services  
class Manager:
    def displayMainMenu(self):
        options = {
            'Main Menu': ['1. Generate reports', '2. Modify Members', '3. Modify Providers', '4. Modify Services', '5. Quit']
        }
        df = pd.DataFrame(options)
        df_styled = df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'left'})
        print(tabulate(df_styled.data, headers=df_styled.columns, tablefmt='fancy_grid', showindex=False))
        return int(input("Please enter your choice: "))
    
    def reportsMenu(self):
        options = {
            'Report to generate': ['1. Member report', '2. Provider report', '3. EFT report', '4. Summary report']
        }
        df = pd.DataFrame(options)
        df_styled = df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'left'})
        print(tabulate(df_styled.data, headers=df_styled.columns, tablefmt='fancy_grid', showindex=False))
        return int(input("Please enter your choice: "))
    
    def membersMenu(self):
        options = {
            'Services': ['1. Add Member', '2. Remove Member', '3. Update Member Records', '4. Display Members']
        }
        df = pd.DataFrame(options)
        df_styled = df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'left'})
        print(tabulate(df_styled.data, headers=df_styled.columns, tablefmt='fancy_grid', showindex=False))
        return int(input("Please enter your choice: "))
    
    def providersMenu(self):
        options = {
            'Services': ['1. Add Provider', '2. Remove Provider', '3. Update Provider Records']
        }
        df = pd.DataFrame(options)
        df_styled = df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'left'})
        print(tabulate(df_styled.data, headers=df_styled.columns, tablefmt='fancy_grid', showindex=False))
        return int(input("Please enter your choice: "))
    def servicesMenu(self):
        options = {
            'Services': ['1. Add Service', '2. Remove Service', '3. Update Service Name', '4. Update Service Fee', '5. Display services']
        }
        df = pd.DataFrame(options)
        df_styled = df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'left'})
        print(tabulate(df_styled.data, headers=df_styled.columns, tablefmt='fancy_grid', showindex=False))
        return int(input("Please enter your choice: "))
    
    def menu(self):
        print("Welcome back!")
        while True:
            option = self.displayMainMenu()
            match option:
                case 1:
                    choice = self.reportsMenu()
                case 2:
                    m = Member()
                
                    while True:
                        response = self.membersMenu()
                        if response == 1:
                            m.enter_Member_details()
                        elif response == 2:
                            m.remove_member()
                        elif response == 3:
                            #m.update_provider_records()
                            pass
                        elif response == 4:
                            m.display_members()
                        else:
                            print("Enter a valid option!")
                            continue  # repeat the loop until a valid option is entered
                        break  # exit the loop once a valid option is selected     

                case 3:
                    p = Provider()
                    while True:
                        response = self.providersMenu()
                        if response == 1:
                            p.enter_Provider_details()
                        elif response == 2:
                            p.remove_provider()
                        elif response == 3:
                            p.update_provider()
                        else:
                            print("Enter a valid option!")
                            continue  # repeat the loop until a valid option is entered
                        break  # exit the loop once a valid option is selected         
                case 4:
                    s = Service()
                    while True:
                        response = self.servicesMenu()
                        if response == 1:
                            s.enter_service_details()
                        elif response == 2:
                            s.remove_service()
                        elif response == 3:
                            s.update_service_name()
                        elif response == 4:
                            s.update_service_fee()
                        elif response == 5:
                            s.display_services()
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
    