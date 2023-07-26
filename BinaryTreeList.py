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


bst = BinaryTree(8)
print(bst.insert_node("Drinks"))
print(bst.insert_node("Hot"))
print(bst.insert_node("Right"))
