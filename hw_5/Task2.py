class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, item):
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            new_tail = Node(item, None)
            self.tail.next = new_tail
            self.tail = new_tail

        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None

        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None

        return self.head.value

    def is_empty(self) -> bool:
        return self.size == 0

    def size(self):
        return self.size
