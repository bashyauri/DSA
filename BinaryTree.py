class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


treeNode = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
treeNode.left = leftChild  # type: ignore
treeNode.right = rightChild  # type: ignore


def preOrderTraversal(root_node):
    if root_node is None:
        return
    print(root_node.value)
    preOrderTraversal(root_node.left)
    preOrderTraversal(root_node.right)


preOrderTraversal(treeNode)
