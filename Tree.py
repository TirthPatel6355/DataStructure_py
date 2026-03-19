class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    # get parent level to print space
    def get_level(self):
        level = 0
        p=self.parent
        while p:
            level += 1
            p=p.parent
        return level


    def print_tree(self):
        for i in range(0,self.get_level()):
            print("  ",end="")
        print(self.data)
        for child in self.children:
             child.print_tree()



def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("iphone"))
    cellphone.add_child(TreeNode("Google pixel"))
    cellphone.add_child(TreeNode("vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
