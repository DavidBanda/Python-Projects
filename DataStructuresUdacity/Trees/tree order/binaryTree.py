class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.nodes = ""

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""

        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        self.preorder_print(self.root)
        print(self.nodes[:-1])

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""

        # if find_val == start.value:
        #     return True
        #
        # if start.left:
        #     if self.preorder_search(start.left, find_val):
        #         return True
        #
        # if start.right:
        #     if self.preorder_search(start.right, find_val):
        #         return True
        #
        # return False

        if start:
            if find_val == start.value:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start):
        """Helper method - use this to create a
        recursive print solution."""
        self.nodes += "{}-".format(start.value)

        if start.left:
            self.preorder_print(start.left)

        if start.right:
            self.preorder_print(start.right)


n1 = Node(1)
n2 = Node(3)
n3 = Node(5)
n4 = Node(7)
n5 = Node(9)

b1 = BinaryTree(n1)

b1.root.left = n2
b1.root.right = n3
b1.root.left.left = n4
b1.root.right.right = n5

print(b1.search(1))
b1.print_tree()



