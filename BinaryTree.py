from operator import truediv


class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.add_child(data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.add_child(data)

    def in_order(self):
        element = []

        # visit left tree
        if self.left:
            element+= self.left.in_order()

        # visit base Node
        element.append(self.data)

        # visit right tree
        if self.right:
            element+= self.right.in_order()

        return element

    def pre_order(self):
        element = []
        # visit base Node
        element.append(self.data)

        # visit left tree
        if self.left:
            element += self.left.pre_order()

        # visit right tree
        if self.right:
            element += self.right.pre_order()

        return element

    def post_order(self):
        element = []
        # visit left tree
        if self.left:
            element+= self.left.post_order()

        # visit right tree
        if self.right:
            element+= self.right.post_order()

        # visit base Node
        element.append(self.data)
        return element

    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

#     delete node using max of left subtree
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            # min_value = self.right.find_min()
            # self.data = min_value
            # self.right = self.right.delete(min_value)
            max = self.left.find_max()
            self.data = max
            self.left =self.left.delete(max)

        return self




    def find_max(self):
        if self.right == None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left == None:
            return self.data
        return self.left.find_min()

def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = [17,4,1,20,9,23,18,34,13,19]
    numbers_tree = build_tree(numbers)
    # print(numbers_tree.pre_order())
    # print(numbers_tree.search(24))
    numbers_tree.delete(20)
    print(numbers_tree.in_order())
