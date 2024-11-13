class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None  # Start with an empty stack

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head  # New node points to the current head
        self.head = new_node       # Head becomes the new node

    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return None
        data = self.head.data
        self.head = self.head.next  # Move head to the next node
        return data

    def peek(self):
        return self.head.data if self.head else None
# Stack Example
stack = Stack()
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
