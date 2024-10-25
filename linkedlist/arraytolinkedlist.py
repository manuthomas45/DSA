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
            return
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=new_node
    def array_to_linkedlist(self,arr):
        if not arr:
            return None
        self.head=Node(arr[0])
        current=self.head
        for v in arr[1:]:
            current.next=Node(v)
            current=current.next 
        return self.head
     
    def linked_list_to_array(self):
        arr=[]
        current=self.head
        while current:
            arr.append(current.data)
            current=current.next
        return arr


    def display(self):
        if self.head is None:
            print("there is no node in the linkedlist")
        else:
            current=self.head
            while current:
                print(current.data,end="->")
                current=current.next
ll=Linkedlist()
ll.append(4)
ll.append(5)
ll.append(8)
ll.display()
arr=[10,20,30,40]
l2=Linkedlist()
l2.array_to_linkedlist(arr)
l2.display()
print(ll.linked_list_to_array())












