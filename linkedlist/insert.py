# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkdelist:
#     def __init__(self):
#         self.head=None
#     def add_at_biginning(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data,end=" -> ")
#             current=current.next
#         print("NONe")
#     def add_at_end(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#             return
#         last=self.head
#         while last.next:
#             last=last.next
#         last.next=new_node

# m=Linkdelist()
# m.add_at_biginning(10)
# m.add_at_biginning(1)
# m.add_at_end(4)
# m.add_at_end(8)
# m.display()
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    def add_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def display(self):
        current=self.head
        if current:
            print(current.data,end="->")
            current=current.next
        print("none")
    def add_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            print("hai")
        else:
            last=self.head
            while last.next:
                print("hoi")
                last=last.next
            last.next=new_node

l=Linkedlist()
# l.add_at_beginning(10)
l.add_at_end(1)
l.add_at_end(4)
l.display()
