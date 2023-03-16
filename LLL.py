# The purpose of this file is to implement the Linear Linked List
# methods: insert, retrieve, display and remove
from datetime import datetime
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
        with open(filename, "a") as f:
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