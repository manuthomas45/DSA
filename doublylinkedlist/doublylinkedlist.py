class Node:
    def __init__(self, data):
        self.data = data  # Data field
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head to None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Display the list in forward direction
    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(None)

    # Display the list in backward direction
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return
        last = self.head
        while last.next:
            last = last.next
        while last:
            print(last.data, end=" -> ")
            last = last.prev
        print(None)

    # Delete from the beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # Delete from the end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            last = self.head
            while last.next:
                last = last.next
            last.prev.next = None
# Creating a doubly linked list
dll = DoublyLinkedList()

# Inserting nodes
dll.insert_at_beginning(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_beginning(5)

# Displaying the list
print("Forward traversal:")
dll.display_forward()

print("Backward traversal:")
dll.display_backward()

# Deleting nodes
dll.delete_from_beginning()
dll.delete_from_end()

# Displaying after deletion
print("After deletions:")
dll.display_forward()
