# The purpose of this file is to implement the Linear Linked List
# methods: insert, retrieve, display and remove
from datetime import datetime
'''
from ChocAn import *
import Member

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
    '''
class RecordNode:
    def __init__(self, current_date_time, service_date, provider_number, member_number, service_code, comments):
        self.current_date_time = current_date_time
        self.service_date = service_date
        self.provider_number = provider_number
        self.member_number = member_number
        self.service_code = service_code
        self.comments = comments
        self.next = None
        
class RecordList:
    def __init__(self):
        self.head = None
        
    def add_record(self, current_date_time, service_date, provider_number, member_number, service_code, comments):
        new_node = RecordNode(current_date_time, service_date, provider_number, member_number, service_code, comments)
        
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            
    def display_records(self):
        current_node = self.head
        while current_node is not None:
            print("Current date and time:", current_node.current_date_time)
            print("Date service was provided:", current_node.service_date)
            print("Provider number:", current_node.provider_number)
            print("Member number:", current_node.member_number)
            print("Service code:", current_node.service_code)
            print("Comments:", current_node.comments)
            print()
            current_node = current_node.next

    def save_to_file(self, filename):
        current_node = self.head
        with open(filename, "w") as f:
            while current_node is not None:
                dt = datetime.strptime(str(current_node.current_date_time), "%Y-%m-%d %H:%M:%S")
                sd = datetime.strptime(str(current_node.service_date),"%Y-%m-%d")
                f.write(dt.strftime("%Y-%m-%d %H:%M:%S")+ "," +
                        sd.strftime("%Y-%m-%d")+ "," +
                        current_node.provider_number + "," +
                        current_node.member_number + "," +
                        current_node.service_code + "," +
                        current_node.comments + "\n")
                current_node = current_node.next
    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
          
            current_node = current_node.next
                
    def load_from_file(self, filename):
        with open(filename, "r") as f:
            for line in f:
                fields = line.strip().split(",")
                current_date_time = fields[0]
                service_date = fields[1]
                provider_number = fields[2]
                member_number = fields[3]
                service_code = fields[4]
                comments = fields[5]
                self.add_record(current_date_time, service_date, provider_number, member_number, service_code, comments)