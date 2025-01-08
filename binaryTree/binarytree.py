from collections import deque
class BinarySerchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):

        if self.data==data:
            return 
        if self.data>data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySerchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySerchTreeNode(data)
    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    def bfs(self):
        queue=deque([self])
        res=[]
        while queue:
            currenet=queue.popleft()
            res.append(currenet.data)
            if currenet.left:
                queue.append(currenet.left)
            if currenet.right:
                queue.append(currenet.right)
        return res
    def search(self,val):
        if self.data==val:
            return True
        if self.data>val:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if self.data<val:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def find_max(self):
        # if  self.right is None:
        #     return self.data
        # return self.right.find_max()
        while self.right:
            self=self.right
        return self.data
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
        # while self.left:
        #     self=self.left
        # return self.data
    def delete(self,val):
        if self.data>val:
            if self.left:
                self.left=self.left.delete(val)
        elif self.data<val:
            if self.right:
                self.right=self.right.delete(val) 
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            minval=self.right.find_min()
            self.data=minval
            self.right=self.right.delete(minval)
        return self
    def bfs(self):
        # Initialize a queue
        queue = deque([self])
        result = []
        while queue:
            # Dequeue the front node
            current = queue.popleft()
            result.append(current.data)
            # Enqueue children
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
    def sum(self):
        total=self.data
        if self.left:
            total+=self.left.sum()
            
        if self.right:
            total+=self.right.sum()
        return total
    def count_left_subtree(self):
        if not self.left:
            return 0
        return self.left.count_nodes()
    
    def count_nodes(self):#no of left node
        count = 1  # Count the current node
        if self.left:
            count += self.left.count_nodes()
        if self.right:
            count += self.right.count_nodes()
        return count 
    
    def max_in_leftsubtree(self):
        if not self.left:
            return None
        current=self.left
        while current.right:
            current=current.right
        return current.data
    def is_bst(self, min_value=float('-inf'), max_value=float('inf')):
        # Check if current node's value is within the allowed range
        if not (min_value < self.data < max_value):
            return False
        
        # Check left subtree if it exists
        if self.left and not self.left.is_bst(min_value, self.data):
            return False

        # Check right subtree if it exists
        if self.right and not self.right.is_bst(self.data, max_value):
            return False

        return True
    def level(self):
        level=1
        while self.left:
            self=self.left
            level+=1
        return level
    def find_level(self, value, level=0):
        if self.data == value:  # Found the node
            return level
        if value < self.data and self.left:  # Check left subtree
            return self.left.find_level(value, level + 1)
        if value > self.data and self.right:  # Check right subtree
            return self.right.find_level(value, level + 1)
        return -1  # If value is not found
    def height(self):
        if self is None:
            return -1  # Height of an empty tree is -1
        left_height = self.left.height() if self.left else -1
        right_height = self.right.height() if self.right else -1
        return 1 + max(left_height, right_height)
    def find_closest(self, target):
        closest = self.data  # Initialize closest with the root value
        current = self
        while current:
            # Update closest if the current node is closer to the target
            if abs(target - current.data) < abs(target - closest):
                closest = current.data
            # Move left or right depending on the target value
            if target < current.data:
                current = current.left
            elif target > current.data:
                current = current.right
            else:
                break  # Exact match found
        return closest
   


    def find_kth_largest(self, k):
        self.k = k
        self.result = None
        self._reverse_inorder()
        return self.result

    def _reverse_inorder(self):
        if self.right:
            self.right._reverse_inorder()
        self.k -= 1
        if self.k == 0:
            self.result = self.data
            return
        if self.left:
            self.left._reverse_inorder()
    def print_even(self):
        if self.left:
            self.left.print_even()
        if self.data % 2 == 0:  # Check if the value is even
            print(self.data, end=" ")
        if self.right:
            self.right.print_even()
    def has_subtree(self, value):
        if self.data == value:
            # Check if it has any children
            if self.left or self.right:
                print(f"The node with value {value} has a subtree.")
                return True
            else:
                print(f"The node with value {value} does not have a subtree.")
                return False
        if self.data > value and self.left:
            return self.left.has_subtree(value)
        elif self.data < value and self.right:
            return self.right.has_subtree(value)
        else:
            print(f"Value {value} not found in the BST.")
            return False
def are_identical(root1, root2):
    # If both trees are empty, they are identical
    if not root1 and not root2:
        return True

    # If one tree is empty and the other is not, they are not identical
    if not root1 or not root2:
        return False

    # Check if the current nodes' data are the same
    # and recursively check left and right subtrees
    return (root1.data == root2.data and are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right))
#identical,second largest,target element exit,
numbers = [4,1,12,14,20,7,88,23]
# we can give string also instead of number and tree here it will be only set if you give same value it will not take
root = BinarySerchTreeNode(numbers[0])  # Initialize tree with the first element
for num in numbers[1:]:
    root.add_child(num)
root.delete(4)
print(root.in_order_traversal())
# print(root.pre_order_traversal())
# print(root.post_order_traversal())
# print(root.search(677))
# print(root.find_max())
# print(root.find_min())
# print(root.sum())
# print(root.count_left_subtree())
# print(root.max_in_leftsubtree())
#check bfs and dfs
      
