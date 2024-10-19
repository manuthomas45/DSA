# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Stores the value of the node
        self.next = None  # Points to the next node in the list (initially None)

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # The first node of the linked list (initially None)

    # Add a node to the end of the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:
            self.head = new_node  # If list is empty, the new node becomes the head
        else:
            last = self.head
            while last.next:
                last = last.next  # Traverse to the end of the list
            last.next = new_node  # Attach the new node at the end

    # Display the linked list elements
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of the list

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3 -> None
# ----------------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("The list is empty.")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("The list is empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        last = self.head
        while last.next.next:
            last = last.next
        last.next = None

    def delete_at_position(self, position):
        if self.head is None:
            print("The list is empty.")
            return
        if position == 0:
            self.delete_at_beginning()
            return
        current = self.head
        for i in range(position - 1):
            if current.next is None:
                print("Position is out of bounds.")
                return
            current = current.next
        if current.next is None:
            print("Position is out of bounds.")
            return
        current.next = current.next.next

    def delete_at_center(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return
        slow = self.head
        fast = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(30)
llist.append(40)
llist.append(50)

print("Original List:")
llist.print_list()

print("Delete at beginning:")
llist.delete_at_beginning()
llist.print_list()

print("Delete at end:")
llist.delete_at_end()
llist.print_list()

print("Delete at position 1 (index):")
llist.delete_at_position(1)
llist.print_list()

print("Delete at center:")
llist.delete_at_center()
llist.print_list()
