class TreeNode:
    def __init__(self, value):
        self.value = value        # Stores the node's value
        self.children = []        # Initializes an empty list to store child nodes

    def add_child(self, child_node):
        self.children.append(child_node)  # Adds the provided node to the children list

    def print_tree(self, level=0):
        print(" " * level * 2 + str(self.value))  # Indents based on tree depth, then prints value
        for child in self.children:
            child.print_tree(level + 1)  # Recursively calls print for each child at the next level

# Example usage
root = TreeNode("Root")            # Creates the root node with value "Root"
child1 = TreeNode("Child 1")       # Creates a child node with value "Child 1"
child2 = TreeNode("Child 2")       # Creates a second child node with value "Child 2"

root.add_child(child1)             # Adds "Child 1" to the root's children
root.add_child(child2)             # Adds "Child 2" to the root's children

child1.add_child(TreeNode("Child 1.1"))  # Adds a child to "Child 1"
child2.add_child(TreeNode("Child 2.1"))  # Adds a child to "Child 2"
child2.add_child(TreeNode("Child 2.2"))  # Adds another child to "Child 2"

root.print_tree()                  # Prints the entire tree, showing hierarchy
