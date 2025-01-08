from collections import deque
class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data==data:
            return 
        if self.data>data:
            if self.left:
                self.left.insert(data)
            else:
                self.left=BinarySearchTree(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right=BinarySearchTree(data)
    def search(self,val):
        if self.data==val: 
            print("found")
            return 
        if self.data>val:
            if self.left:
                self.left.search(val)
            else:
                print("not found")
        else:
            if self.right:
                 self.right.search(val)
            else:
                print("not found")
    def inorder(self):
        ele=[]
        if self.left:
            ele+=self.left.inorder()
        ele.append(self.data)
        if self.right:
            ele+=self.right.inorder()
        return ele
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

        
bst=BinarySearchTree(40)
num=[23,25,16,38,94,74,65,2]
for i in num:
    bst.insert(i)
# bst.search(25)
print(bst.inorder())
print(bst.bfs())