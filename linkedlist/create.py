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
            self.head = new_node
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=new_node
    def display(self):
        current=self.head
        if current is None:
            print("no nodes")
        else:
            while current:
                print(current.data, end ="->")
                current=current.next
l=Linkedlist()
l.append(5)
l.append(6)
l.append(7)
l.display()