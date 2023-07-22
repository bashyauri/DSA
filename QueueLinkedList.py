class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return " ".join(values)

    def enqueue(self, value):
        new_node = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = new_node
            self.linkedList.tail = new_node
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node

    def dequeue(self):
        if self.linkedList.head is None:
            return "The LinkedList is Empty"
        node_to_remove = self.linkedList.head
        self.linkedList.head = node_to_remove.next
        node_to_remove.next = None
        return node_to_remove

    def peek(self):
        if self.linkedList.head is None:
            return "The LinkedList is Empty"
        return self.linkedList.head

    def is_empty(self):
        if self.linkedList.head is None:
            return True
        return False


# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.is_empty())
