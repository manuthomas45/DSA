class Node:
    def __init__(self, data):
        self.data = data  # Node's data
        self.next = None  # Pointer to the next node

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # Method to insert a node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point to itself
        else:
            temp = self.head
            while temp.next != self.head:  # Traverse till the last node
                temp = temp.next
            temp.next = new_node  # Last node points to the new node
            new_node.next = self.head  # New node points to the head

    # Method to insert a node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:  # Find the last node
                temp = temp.next
            temp.next = new_node  # Last node now points to the new first node
            self.head = new_node  # Update the head to the new node

    # Method to traverse the list
    def traverse(self):
        if not self.head:
            print("The list is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print(f"Head ({self.head.data})")  # To indicate it's circular

    # Method to delete the node at the beginning
    def delete_at_beginning(self):
        if not self.head:
            print("The list is empty.")
            return
        if self.head.next == self.head:  # Only one node
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:  # Find the last node
                temp = temp.next
            temp.next = self.head.next  # Last node now points to the second node
            self.head = self.head.next  # Update head to the second node

    # Method to delete the node at the end
    def delete_at_end(self):
        if not self.head:
            print("The list is empty.")
            return
        if self.head.next == self.head:  # Only one node
            self.head = None
        else:
            temp = self.head
            prev = None
            while temp.next != self.head:  # Traverse to the last node
                prev = temp
                temp = temp.next
            prev.next = self.head  # Second last node now points to the head

# Example usage
csll = CircularSinglyLinkedList()
csll.insert_at_end(10)
csll.insert_at_end(20)
csll.insert_at_end(30)
csll.insert_at_beginning(5)

csll.traverse()  # Output: 5 -> 10 -> 20 -> 30 -> Head (5)

csll.delete_at_beginning()
csll.traverse()  # Output: 10 -> 20 -> 30 -> Head (10)

csll.delete_at_end()
csll.traverse()  # Output: 10 -> 20 -> Head (10)
