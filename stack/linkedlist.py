class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return "Stack Underflow"
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data

    def display(self):
        current = self.head
        if current is None:
            print("Stack is empty")
        else:
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

# Example usage
stack = Linkedlist()
stack.push(5)
stack.push(6)
stack.push(7)
stack.display()  # Output: 7 -> 6 -> 5 -> None
print("Popped:", stack.pop())  # Output: Popped: 7
stack.display()  # Output: 6 -> 5 -> None
