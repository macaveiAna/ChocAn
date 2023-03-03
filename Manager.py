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
                print("2.Provider report")
            case 2:
                print("What do you want to do?")
                print("1.Add member")
                print("2.Remove member")
                print("3.Update member records")
            case 3:
                print("What do you want to do?")
                print("1.Add provider")
                print("2.Remove provider")
                print("3.Update provider records")
            case 4:
                print("What do you want to do?")
                print("1.Add service")
                print("2.Remove service")
                print("3.Update services")
    def load(self):
        self.menu()
    