from Provider import Provider
from Member import *
from Service import *
#generate different reports for provider and member
#able to add member,delete member, same with provider and able to also do the same with services  
class Manager:
    def __init__(self):
        pass
    def getOption(self):
        option = int(input("> "))
        if (option < 0 or option > 4):
            print("Please enter a valid option!")
            self.getOption()
        return option
    def menu(self):
        print("Welcome back!")
        print("Which service do you want?")
        print("1.Generate reports")
        print("2.Modify Members")
        print("3.Modify Providers")
        print("4.Modify Services")
        option = self.getOption()
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
               p = Provider.Provider()
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

    def load(self):
        self.menu()
    