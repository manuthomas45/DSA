class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class doublyll:
    def __init__(self):
        self.head=None
    def print_dll(self):
        if self.head is None:
            print("dll is empty")
        else:
            current=self.head
            while current is not None:
                print(current.data,"-->",end=" ")
                current=current.nref
    def print_dll_reverse(self):
        if self.head is None:
            print("dll is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                
                print(n.data,"-->",end=" ")
                n=n.pref
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("dll is not empty")
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    def add_after(self,data,x):
        if self.head is None:
            print("dll is empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("given node is not present")
            else:
                new_node=Node(data)
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node
    def add_before(self,data,x):
        if self.head is None:
            print("dll is empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("given node is not present")
            else:
                new_node=Node(data)
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                n.pref=new_node
    def delete_at_beginning(self):
        if self.head is None:
            print("dll is empty")
            return 
        if self.head.nref is None:
            self.head=None
        else:
            self.head=self.head.nref
            self.head.pref=None
    def delete_at_end(self):
        if self.head is None:
            print("dll is empty")
            return
        if self.head.nref is None:
            self.head=None

        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
    def delete_value(self,x):
        if self.head is None:
            print("dll is empty")
            return
        if self.head.nref is None:
            if x==self.head.data:
                self.head=None
            else:
                print("x is not present in the dll")
            return
        if self.head.data==x:
            self.head=self.head.nref
            self.head.prev=None
            return
        n=self.head
        while n.nref is not None:
            if x == n.data:
                
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref=n.pref
            n.pref.nref=n.nref
        else:
            if n.data==x:
                n.pref.nref=None
            else:
                print("x is not present in the linkedlist")












dl1=doublyll()
dl1.insert_empty(5)
dl1.add_begin(6)
dl1.add_end(77)
dl1.add_after(55,5)
dl1.add_before(66,5)
# dl1.delete_at_beginning()
# dl1.delete_at_end()
dl1.delete_value(64)
dl1.print_dll()
print("\n")
dl1.print_dll_reverse()






















