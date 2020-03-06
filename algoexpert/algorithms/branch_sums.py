# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root):
    sums = []
    recursive_branch_sum(root, 0, sums)
    return sums


def recursive_branch_sum(node, carry, sums):
    if node is None:
        return

    new_carry = node.value + carry
    if node.left is None and node.right is None:
        sums.append(new_carry)
        return

    recursive_branch_sum(node.left, new_carry, sums)
    recursive_branch_sum(node.right, new_carry, sums)









