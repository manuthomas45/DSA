class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=new_node
    def insert_after_avalue(self,target,data):
        new_node=Node(data)
        current=self.head
        while current and current.data!=target:
            current=current.next

        if current is None:
            print("target is not found")
        else:
            new_node.next=current.next
            current.next=new_node
        
    def insert_before_avalue(self,target,data):
            new_node=Node(data)
            if self.head is None:
                print ("target is not in the linkedlist")
            if self.head.data==target:
                new_node.next=self.head
                self.head=new_node
            current=self.head
            prev=0
            if current and current!=target:
                prev=current
                current=current.next
            else:
                if current.next is None:
                    print("target is not in the linkedlist")
                else:
                    new_node.next=current
                    prev.next=new_node
    def insert_at_position(self, position, data):
        new_node=Node(data)
        if position ==1:
            new_node.next=self.head
            self.head=new_node
            return 
        current=self.head
        for _ in range(position-2):
            if current is None:
                print("out of range")
                return
            current=current.next
        if current:
            new_node.next=current.next
            current.next=new_node
    
    def insert_at_middle(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        s=self.head
        f=self.head
        prev=None
        while f and f.next:
            f=f.next.next
            prev=s
            s=s.next
        print(s.data)
        new_node.next=s
        if prev:
            prev.next=new_node
        else:
            self.head=new_node

        

    def display(self):
        current=self.head
        if current is None:
            print("there is no node in the linkedlist")
        else:
            while current:
                print(current.data,end="->")
                current=current.next
l=LinkedList()
l.append(70)
l.append(60)
l.append(50)
l.append(40)
l.append(408)
l.append(30)
l.append(20)
l.insert_after_avalue(40,10)
l.insert_before_avalue(40,25)
l.insert_at_position(8,4)
l.insert_at_middle(88)
l.display()




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # Insertion at the end
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             last = self.head
#             while last.next:
#                 last = last.next
#             last.next = new_node

#     # Insertion before a specific value
#     def insert_before_value(self, target, data):
#         new_node = Node(data)
#         if self.head is None:
#             print(f"List is empty. Cannot insert before {target}")
#             return

#         if self.head.data == target:  # If the target is the head
#             new_node.next = self.head
#             self.head = new_node
#             return

#         prev = None
#         current = self.head
#         while current and current.data != target:
#             prev = current
#             current = current.next

#         if current is None:
#             print(f"Value {target} not found in the list")
#         else:
#             new_node.next = current
#             prev.next = new_node

#     # Insertion after a specific value
#     def insert_after_value(self, target, data):
#         new_node = Node(data)
#         current = self.head

#         while current and current.data != target:
#             current = current.next

#         if current is None:
#             print(f"Value {target} not found in the list")
#         else:
#             new_node.next = current.next
#             current.next = new_node

#     # Insertion at a specific position (1-indexed)
#     def insert_at_position(self, position, data):
#         new_node = Node(data)
#         if position == 1:  # Insert at the head
#             new_node.next = self.head
#             self.head = new_node
#             return

#         current = self.head
#         for _ in range(position - 2):  # Traverse to the node before the position
#             if current is None:
#                 print(f"Position {position} out of bounds")
#                 return
#             current = current.next

#         if current is None:
#             print(f"Position {position} out of bounds")
#         else:
#             new_node.next = current.next
#             current.next = new_node

#     # Display linked list
#     def display(self):
#         current = self.head
#         if current is None:
#             print("The list is empty")
#             return
#         while current:
#             print(current.data, end=" -> " if current.next else "\n")
#             current = current.next

# # Example Usage
# ll = LinkedList()

# # Append nodes
# ll.append(10)
# ll.append(20)
# ll.append(40)

# # Insert before value
# ll.insert_before_value(20, 15)

# # Insert after value
# ll.insert_after_value(40, 50)

# # Insert at position
# ll.insert_at_position(2, 12)

# ll.display()
