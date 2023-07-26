from QueueLinkedList import Queue, LinkedList


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


treeNode = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
treeNode.left = leftChild  # type: ignore
treeNode.right = rightChild  # type: ignore
leftChild.left = tea
leftChild.right = coffee


def preOrderTraversal(root_node):
    if root_node is None:
        return
    print(root_node.value)
    preOrderTraversal(root_node.left)
    preOrderTraversal(root_node.right)


def inOrderTraversal(root_node):
    if root_node is None:
        return

    inOrderTraversal(root_node.left)
    print(root_node.value)
    inOrderTraversal(root_node.right)


def postOrderTraversal(root_node):
    if root_node is None:
        return
    postOrderTraversal(root_node.left)
    postOrderTraversal(root_node.right)
    print(root_node.value)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.is_empty()):
            current_node = customQueue.dequeue()

            if current_node.value.left:
                customQueue.enqueue(current_node.value.left)

            if current_node.value.right:
                customQueue.enqueue(current_node.value.right)


def search_node(root_node, node):
    q = Queue()

    if root_node is None:
        return "Empty List"
    q.enqueue(root_node)
    while not q.is_empty():
        current_node = q.dequeue()
        if current_node.value.value == node:
            return True
        if current_node.value.left:
            q.enqueue(current_node.value.left)
        if current_node.value.right:
            q.enqueue(current_node.value.right)
    return False


def insert_node(root_node, node):
    if root_node is None:
        root_node = node
    else:
        q = Queue()
        q.enqueue(root_node)
        while not q.is_empty():
            current_node = q.dequeue()
            if current_node.value.left:
                q.enqueue(current_node.value.left)
            else:
                current_node.value.left = node
                return True
            if current_node.value.right:
                q.enqueue(current_node.value.right)
            else:
                current_node.value.right = node
                return True


def get_deepest_node(root_node):
    if root_node is None:
        return False
    q = Queue()
    q.enqueue(root_node)
    while not q.is_empty():
        current_node = q.dequeue()
        if current_node.value.left:
            q.enqueue(current_node.value.left)
        if current_node.value.right:
            q.enqueue(current_node.value.right)
    deepest_node = current_node.value
    return deepest_node


def delete_deepest_node(root_node, deepest_node):
    if root_node is None:
        return False
    q = Queue()
    q.enqueue(root_node)
    while not q.is_empty():
        current_node = q.dequeue()

        if current_node.value.value is deepest_node:
            current_node.value.value = None
            return

        if current_node.value.right:
            if current_node.value.right is deepest_node:
                current_node.value.right = None
                return
            else:
                q.enqueue(current_node.value.right)
        if current_node.value.left:
            if current_node.value.left is deepest_node:
                current_node.value.left = None
                return
            else:
                q.enqueue(current_node.value.left)


def delete_node(root_node, node):
    if root_node is None:
        return False
    q = Queue()
    q.enqueue(root_node)
    while not q.is_empty():
        current_node = q.dequeue()

        if current_node.value.value is node:
            deepest_node = get_deepest_node(root_node)
            current_node.value.value = deepest_node.value
            delete_deepest_node(root_node, deepest_node)
            return True
        if current_node.value.left:
            q.enqueue(current_node.value.left)
        if current_node.value.right:
            q.enqueue(current_node.value.right)
    return False


def delete_binary_tree(root_node):
    root_node.value = None
    root_node.left = None
    root_node.right = None
    return "Binary Tree Successfully deleted"


delete_node(treeNode, "Hot")
levelOrderTraversal(treeNode)


# levelOrderTraversal(treeNode)
