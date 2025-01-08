class BinaryserachTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_node(self,data):
        if self.data==data:
            return 
        if self.data>data:
            if self.left:
                self.left.add_node(data)
            else:
                self.left=BinaryserachTree(data)
        else:
            if self.right:
                self.right.add_node(data)
            else:
                self.right=BinaryserachTree(data)
    def inorder(self):
        elements=[]
        if self.left:
            elements+=self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements+=self.right.inorder()
        return elements
    def is_bst(self,min_val=float('-inf'),max_val=float('inf')):
        if not(min_val<self.data<max_val):
            return False
        if self.left and not self.left.is_bst(min_val,self.data):
            return False
        if self.right and not self.right.is_bst(self.data,max_val):
            return False
        return True
    def height(self):
        l_height=1
        while self.left:
            l_height+=1
            self=self.left
        r_height=1
        while self.right:
            r_height+=1
            self=self.right
        return max(l_height,r_height)
num=[23,44,55,12,16,19,44,87,43,77]
bst=BinaryserachTree(num[0])
for i in num[1:]:
    bst.add_node(i)
print(bst.inorder())
print(bst.is_bst())
print(bst.height())