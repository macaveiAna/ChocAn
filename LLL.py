# The purpose of this file is to implement the Linear Linked List
# methods: insert, retrieve, display and remove

from ChocAn import *

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
    '''
     #loads contents of the file   
    def load(self):
        file = open("MemberDirectory.txt", "r")
        
     
        for line in file:
            m = Member()
            m.member_id = line[0]
            m.member_name = line[1] + " " + line[2]
            #self._head = self._head.set_next(m) 
            m.set_next(self._head)
            self._head = m
            
            #item = line.split('|')   
            #print(line)
            #self._insert(line) #pass the array into a node structure 
    '''
   
    '''
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
    '''  
 
    
    def _insert(self, item):
        self._head = self._append(self._head, item)
     
    #learn how to append into the file when adding a new member
    def _append(self, head, item):
        m = Member()
        m.member_id = item[0]
        if head == None:
            head = Node() # a new node
          
        
            #still need to finish the rest here 
            #if item[0] == m.member_name:
                #head.data = Member(item[1])
        return head
    
    def display_list(self, head):
        while head != None:
            #head.display()
            print("$%-*s %-*s" % (10, str(head.member_name), 10, head.member_id))
            head = head.get_next()
            
            
    def display(self):
        self.display_list(self._head)