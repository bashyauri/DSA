class BST:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, root_node, value):
        if root_node.value is None:
            root_node.value = value
        else:
            current_node = root_node
            if value <= current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                else:
                    self.insert(current_node.left, value)
            elif value >= current_node:
                if current_node.right is None:
                    current_node.right = BST(value)
                else:
                    self.insert(current_node.right, value)
        return "Node Inserted Successfully"


new_bst = BST(None)
print(new_bst.insert(new_bst, 70))
print(new_bst.insert(new_bst, 60))
print(new_bst.value)
