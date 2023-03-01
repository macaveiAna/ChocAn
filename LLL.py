# The purpose of this file is to implement the Linear Linked List
# methods: insert, retrieve, display and remove

class Node:
    #constructor
    def __init__(self):
        self.data = None
        self._next = None
        
    #destructor
    def __del__(self):
        self._next = None
        
    #get next function
    def get_next(self):
        return self._next
    
    #set next function
    def set_next(self, next):
        self._next = next
        
    def display(self):
        if self.data != None:
            self.data.display()
            
class LLL:
    #default constructor
    def __init__(self):
        self._head = None
        
    def search(self, match):
          return self._search(self._head, match)
        
    #A private function to have the user search for a particular member
    def _search(self, head, match):
        if head == None:
            return False
        if (head.equals(match)):
            print("This member exists.")
            return True
        else:
            print("This member does not exist.")
        return self._search(self._head, match)