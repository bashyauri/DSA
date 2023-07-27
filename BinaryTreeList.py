class BinaryTree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.size = size

    def insert_node(self, value):
        if self.last_used_index + 1 == self.size:
            return "The List is full"
        self.custom_list[self.last_used_index + 1] = value
        self.last_used_index += 1
        return "The value has been successfully inserted"

    def search_node(self, node_value):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == node_value:
                return "Success"
        return "Not Found"

    def preorder_traversal(self, index):
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.preorder_traversal(index * 2)
        self.preorder_traversal(index * 2 + 1)

    def inorder_traversal(self, index):
        if index > self.last_used_index:
            return
        self.inorder_traversal(index * 2)
        print(self.custom_list[index])
        self.inorder_traversal(index * 2 + 1)

    def postorder_traversal(self, index):
        if index > self.last_used_index:
            return
        self.postorder_traversal(index * 2)
        self.postorder_traversal(index * 2 + 1)
        print(self.custom_list[index])


bst = BinaryTree(8)
print(bst.insert_node("Drinks"))
print(bst.insert_node("Hot"))
print(bst.insert_node("Cold"))
print(bst.insert_node("Tea"))
print(bst.insert_node("Coffe"))

bst.postorder_traversal(1)
