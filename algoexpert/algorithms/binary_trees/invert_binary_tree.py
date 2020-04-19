def invertBinaryTree(node):
    queue = [node]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swap(current)
        queue.append(current.left)
        queue.append(current.right)


def swap(node):
    node.left, node.right = node.right, node.left









