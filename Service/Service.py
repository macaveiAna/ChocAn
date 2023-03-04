from Provider import Provider
import json

class Service:
    def __init__(self):
        pass
    
    def add_service(self):
        pass
    
    def validateServiceName(self,name):
        #p = Provider()
        print("Is this the correct service that was provided? ","'",name,"'","[y/n]")
        ans = input("> ")
        if(ans == 'y'):
            '''
            #this code was moved in the Provider.py in an add_comment method
            print("Would you like to enter comments about the service provided? [y/n]")
            ans2 = input("> ")
            if ans2 == 'y':
                print("Please enter a comment (100 characters): ")
                comment = input("> ")
                filename = f"{p.provider_name}.json"
                with open(filename, "w") as file:
                    json.dump(comment, file)
            '''
            
            with open("Service/ProviderDirectory.json") as file:
                data = json.load(file)
            for service in data['services']:
                if service['serviceName'] == name:
                    fees = service['servicePrice']
                    print("Here is the total amount due: ", fees)
                    break
        elif(ans == 'n'):
            print("Try again!")
            p.load_validated()
        else:
            print("Invalid response!")
    
    def printServiceName(self,name):
            print("Service: ", name)
            self.validateServiceName(name)
    