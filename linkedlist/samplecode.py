# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next node as None

# LinkedList class to manage the linked list operations
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    # Method to add an element at the beginning of the list
    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to add an element at the end of the list
    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # If the list is empty, make new_node the head
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node  # Set the last node's next to new_node

    # Method to add an element at a specific position (1-based index)
    def add_at_position(self, data, position):
        if position == 1:  # If adding at the head
            self.add_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        count = 1
        # Traverse the list to the position before the one where we want to insert
        while current and count < position - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position out of range.")
        else:
            new_node.next = current.next  # Link the new node to the next node
            current.next = new_node  # Set current's next to the new node

    # Method to add an element in the center of the list
    def add_in_center(self, data):
        length = self.get_length()
        position = length // 2 + 1  # Middle position
        self.add_at_position(data, position)

    # Method to calculate the length of the linked list
    def get_length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    # Method to display the linked list elements
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a linked list
linked_list = LinkedList()

# Add elements at the end
linked_list.add_at_end(1)
linked_list.add_at_end(2)
linked_list.add_at_end(3)

# Add element at the beginning
linked_list.add_at_beginning(0)

# Add element at a specific position (e.g., at position 3)
linked_list.add_at_position(1.5, 3)

# Add element in the center
linked_list.add_in_center(99)

# Display the linked list
linked_list.display()
