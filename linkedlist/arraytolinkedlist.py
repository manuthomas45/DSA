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















# class Node:
#     def __init__(self, data):
#         self.data = data  # Node's value
#         self.next = None  # Pointer to the next node

# class LinkedList:
#     def __init__(self):
#         self.head = None  # Initially, the list is empty

#     # Convert array to linked list
#     def array_to_linkedlist(self, arr):
#         if not arr:
#             return None
#         self.head = Node(arr[0])  # First element becomes the head
#         current = self.head
#         for value in arr[1:]:
#             current.next = Node(value)  # Create a new node and link it
#             current = current.next
#         return self.head

#     # Convert linked list to array
#     def linkedlist_to_array(self):
#         array = []
#         current = self.head
#         while current:
#             array.append(current.data)  # Append node's data to the list
#             current = current.next
#         return array

#     # Utility function to print the linked list
#     def print_linkedlist(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# # Example usage:

# # Converting an array to a linked list
# arr = [1, 2, 3, 4, 5]
# ll = LinkedList()
# ll.array_to_linkedlist(arr)

# # Printing the linked list
# ll.print_linkedlist()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

# # Converting the linked list back to an array
# new_array = ll.linkedlist_to_array()
# print(new_array)  # Output: [1, 2, 3, 4, 5]
