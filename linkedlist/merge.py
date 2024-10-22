# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     # Function to append a new node at the end of the list
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             last = self.head
#             while last.next:
#                 last = last.next
#             last.next = new_node

#     # Function to append another linked list to this linked list
#     def append_linked_list(self, other_list):
#         if not self.head:
#             self.head = other_list.head
#         else:
#             last = self.head
#             while last.next:
#                 last = last.next
#             last.next = other_list.head
    
#     # Function to display the linked list
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# # Example usage:
# ll1 = LinkedList()
# ll1.append(1)
# ll1.append(2)
# ll1.append(3)

# ll2 = LinkedList()
# ll2.append(4)
# ll2.append(5)
# ll2.append(6)

# print("List 1:")
# ll1.display()

# print("List 2:")
# ll2.display()

# # Appending LinkedList ll2 to LinkedList ll1
# ll1.append_linked_list(ll2)

# print("Merged Linked List:")
# ll1.display()
