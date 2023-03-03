

class Service:
    def __init__(self):
        pass
    '''
    def validateServiceName(self,name):
        print("Is this the correct service that was provided? ","'",name,"'","[y/n]")
        ans = input("> ")
        if(ans == 'y'):
            print("Would you like to enter comments about the service provided? [y/n]")
            ans2 = input("> ")
            if ans2 == 'y':
                p = Provider()
                print("Please enter a comment (100 characters): ")
                comment = input("> ")
                filename = f"{p.provider_name}.json"
                with open(filename, "w") as file:
                    json.dump(comment, file)
            
            with open("Services/ProviderDirectory.json") as file:
                data = json.load(file)
            for service in data['services']:
                if service['serviceName'] == name:
                    fees = service['servicePrice']
                    print("Here is the total amount due: ", fees)
                    break
        elif(ans == 'n'):
            print("Try again!")
            self.load_validated()
        else:
            print("Invalid response!")
    
    
    def printServiceName(self,name):
        print("Service: ", name)
        self.validateServiceName(name)
    '''
    