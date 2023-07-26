class BinaryTree:
    def __init__(self, size):
        self.custom_size = size * [None]
        self.last_used_index = 0
        self.size = size

    def insert_node(self, value):
        if self.last_used_index + 1 == self.size:
            return "The List is full"
        self.custom_size[self.last_used_index + 1] = value
        self.last_used_index += 1
        return "The value has been successfully inserted"


bst = BinaryTree(8)
bst.insert_node("Drinks")
bst.insert_node("Hot")
bst.insert_node("Right")
