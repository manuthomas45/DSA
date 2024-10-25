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


