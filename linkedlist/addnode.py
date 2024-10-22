class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def add_at_starting(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=new_node
    def add_at_end(self,data):
        new_node=Node(data)
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
    def display(self):
        if self.head is None:
            print("no node")
        else:
            current=self.head
            while current:
                print(current.data,end="->")
                current=current.next
l=Linkedlist()
l.append(5)
l.append(9)
l.add_at_starting(3)
l.add_at_starting(44)
l.add_at_end(44)
l.append(7)
l.display()