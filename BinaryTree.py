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


postOrderTraversal(treeNode)
