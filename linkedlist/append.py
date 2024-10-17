class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
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
    def display(self):
        current=self.head
        while  current:
            print(current.data,end="->")
            current=current.next
        print("None")
l=Linkedlist()
# l.display()
l.append(1)
l.append(2)
l.append(3)
l.display()