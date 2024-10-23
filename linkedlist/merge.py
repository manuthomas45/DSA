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
    def merge(self,other_list):
        if not self.head:
            self.head=other_list.head
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=other_list.head


    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next

l1=Linkedlist()
l2=Linkedlist()
l1.append(5)
l1.append(5)
l1.append(5)
print("list1 ")
l1.display()
l2.append(8)
l2.append(5)
l2.append(0)
print("list2")
l2.display()
print("merged linkedlist ")
l1.merge(l2)
l1.display()
























