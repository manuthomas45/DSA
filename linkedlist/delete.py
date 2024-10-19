class Node():
    def __init__(self,data):
        self.next=None
        self.data=data
class LinkedList():
    def __init__(self):
        self.head=None

    def add_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node

        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=new_node

    def display(self):
        if self.head is None:
            print("There is no node in the linkedlist")
        else:
            current=self.head
            while current:
                print(current.data,end="->")
                current=current.next
        
    def add_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def delete_at_beginning(self):
        if self.head is None:
            print("there is no node in the linkedllist")
        else:
            self.head=self.head.next
    def delete_at_end(self):
        if self.head is None:
            print("there is no node in the linkdedlist")
        if self.head.next is None:
            self.head=None
        else:
            last=self.head
            while last.next.next:
                last=last.next
            last.next=None  
    def delete_at_position(self,position):
        if self.head is None:
            print("out of range")
            return
        if position ==0:
            self.delete_at_beginning()
            return 
        current=self.head
        for i in range (position-1):
            if current.next is None:
                print("position is out of range")
                return
            current=current.next
        if current.next is None:
                print("not possible")
                return 
        current.next=current.next.next
    def add_first_and_last(self):
        if self.head is None:
            print("List is empty")
            return None
        
        first_value = self.head.data  # First element

        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        last_value = current.data  # Last element
        
        return first_value + last_value

    # def delete_at_position(self, position):
    #     if self.head is None:
    #         print("The list is empty.")
    #         return
    #     if position == 0:
    #         self.delete_at_beginning()
    #         return
    #     current = self.head
    #     for i in range(position-1):
    #         if current.next is None:
    #             print("Position is out of bounds.")
    #             return
    #         current = current.next
    #     if current.next is None:
    #         print("Position is out of bounds.")
    #         return
    #     current.next = current.next.next
    def insert_after_value(self, target_value, new_data):
        current = self.head
        print("hai")
        # Traverse the list to find the target value
        while current:
            if current.data == target_value:
                break
            current = current.next

        # If the target value is found, insert a new node
        if current is None:
            print(f"Value {target_value} not found in the list.")
            return
        else:
            new_node = Node(new_data)
            new_node.next = current.next
            current.next = new_node
   
l=LinkedList()
l.add_at_end(5)
l.add_at_end(5)
l.add_at_end(6)
l.add_at_end(66)
l.add_at_end(99)
l.add_at_end(97)
l.add_at_end(7)
l.add_at_end(76)
l.add_at_beginning(8)
l.add_at_beginning(87)
l.delete_at_beginning()
l.delete_at_end()
l.delete_at_position(3)
l.display()
result = l.add_first_and_last()
l.insert_after_value(99, 25)

print(result)

