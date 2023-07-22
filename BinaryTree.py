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


def levelOrderTraversal(root_node):
    if root_node is None:
        return
    q = Queue()
    q.enqueue(root_node)
    while q.linkedList.head:
        root = q.dequeue()
        print(root.value.value)
        if root.value.left:
            q.enqueue(root.value.left)
        if root.value.right:
            q.enqueue(root.value.right)


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


# def search_node(node):
#     queue = Queue()
#     head_node = queue.linkedList.head

#     if head_node is None:
#         return "Empty Linked List"
#     queue.enqueue(head_node)
#     while not queue.is_empty():
#         current_node = queue.dequeue()
#         if current_node.value.value == node:
#             return True
#         if current_node.value.left:
#             queue.enqueue(current_node.value.left)
#         if current_node.value.right:
#             queue.enqueue(current_node.value.right)
#     return False


print(search_node(treeNode, "Hot"))
