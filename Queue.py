# create a queue using an array without size limit
class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        value = [str(x) for x in self.items]
        return " ".join(value)

    def isEmpty(self):
        if self.items == []:
            return True
        return False

    def enqueue(self, value):
        self.items.append(value)
        return "Element is inserted at the end of the Queue"

    def dequeue(self):
        if self.isEmpty():
            return "The List is Empty"
        value_to_dequeue = self.items[0]
        self.items.pop(0)
        return value_to_dequeue

    def peek(self):
        if self.isEmpty():
            return "The List is Empty"
        return self.items[0]

    def delete(self):
        self.items = []


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    queue.delete()
    print(queue)
    queue.isEmpty()
