
def findClosestValueInBst(tree, target):

    current_closest_value = tree

    while tree is not None:
        if abs(current_closest_value.value - target) > abs(tree.value - target):
            current_closest_value = tree

        if tree.value < target:
            tree = tree.right
        elif tree.value > target:
            tree = tree.left
        else:
            break

    return current_closest_value.value















