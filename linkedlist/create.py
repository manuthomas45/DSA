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
            last=new_node

    def display(self):
        current=self.head
        if current:
            print(current.data,end="->")
            current=current.next
        

