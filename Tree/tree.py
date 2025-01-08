class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 2
        # prefix = spaces + "|__" if self.parent else ""
        print(spaces+self.data)
        for child in self.children:
            child.print_tree()


# Build and display the tree
root = TreeNode("Electronics")

laptop = TreeNode("Laptop")
laptop.add_child(TreeNode("Mac"))
laptop.add_child(TreeNode("Surface"))
laptop.add_child(TreeNode("Thinkpad"))

cellphone = TreeNode("Cellphone")
cellphone.add_child(TreeNode("iPhone"))
cellphone.add_child(TreeNode("Google Pixel"))
cellphone.add_child(TreeNode("Vivo"))

tv = TreeNode("TV")
tv.add_child(TreeNode("Samsung"))
tv.add_child(TreeNode("LG"))

root.add_child(laptop)
root.add_child(cellphone)
root.add_child(tv)

root.print_tree()
rot=TreeNode("brototype")
batch=TreeNode("190")
# 187=TreeNode()
rot.add_child(batch)
batch.add_child(TreeNode("manu"))
batch.add_child(TreeNode("naveen"))
saniya=TreeNode("saniya")
batch.add_child(saniya)
saniya.add_child(TreeNode("anadhakrishan"))
saniya.add_child(TreeNode("amal"))


rot.add_child(TreeNode("187"))
rot.print_tree()