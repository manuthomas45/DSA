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
    def print_reverse(self,node):
        if node is None:
            return 
        self.print_reverse(node.next)
        print(node.data,end="->")

    def display_reverse(self):
        print("Linkedlist in reverse order")
        self.print_reverse(self.head)
    
l=LinkedList()
l.append(5)
l.append(59)
l.append(80)
l.display_reverse()
