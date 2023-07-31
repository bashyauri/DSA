from QueueLinkedList import Queue


class AVL:
    def __int__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

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


avl_tree = AVL(10)
