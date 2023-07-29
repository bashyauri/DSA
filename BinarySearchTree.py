from QueueLinkedList import Queue


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
            elif value >= current_node.value:
                if current_node.right is None:
                    current_node.right = BST(value)
                else:
                    self.insert(current_node.right, value)
        return "Node Inserted Successfully"

    def preorder_traversal(self, root_node):
        if root_node is None:
            return "Empty"
        current_node = root_node
        print(current_node.value)
        self.preorder_traversal(current_node.left)
        self.preorder_traversal(current_node.right)

    def inorder_traversal(self, root_node):
        if root_node is None:
            return
        current_node = root_node
        self.inorder_traversal(current_node.left)
        print(current_node.value)
        self.inorder_traversal(current_node.right)

    def postorder_traversal(self, root_node):
        if root_node is None:
            return
        current_node = root_node
        self.postorder_traversal(current_node.left)
        self.postorder_traversal(current_node.right)
        print(current_node.value)

    def levelorder_traversal(self, root_node):
        if root_node is None:
            return
        q = Queue()
        q.enqueue(root_node)
        while not q.is_empty():
            current_node = q.dequeue()
            print(current_node.value.value)
            if current_node.value.left:
                q.enqueue(current_node.value.left)
            if current_node.value.right:
                q.enqueue(current_node.value.right)

    def search_node(self, root_node, value):
        if root_node is None:
            return False
        current_node = root_node
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.search_node(current_node.left, value)
        elif value > current_node.value:
            return self.search_node(current_node.right, value)

    def get_min(self, root_node):
        current_node = root_node
        while current_node.left:
            current_node = current_node.left
        return current_node

    def delete_node(self, root_node, value):
        if root_node is None:
            return root_node
        current_node = root_node
        if value < current_node.value:
            current_node.left = self.delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.delete_node(current_node.right, value)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            deepest_node = self.get_min(current_node.right)
            current_node.value = deepest_node.value
            current_node.right = self.delete_node(
                current_node.right, deepest_node.value
            )
        return current_node


new_bst = BST(None)
print(new_bst.insert(new_bst, 70))
print(new_bst.insert(new_bst, 50))
print(new_bst.insert(new_bst, 90))
print(new_bst.insert(new_bst, 30))
print(new_bst.insert(new_bst, 60))
print(new_bst.insert(new_bst, 80))
print(new_bst.insert(new_bst, 100))
print(new_bst.insert(new_bst, 20))
print(new_bst.insert(new_bst, 40))
new_bst.delete_node(new_bst, 50)
new_bst.inorder_traversal(new_bst)
