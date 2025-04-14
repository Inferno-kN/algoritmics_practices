class PrintDocument:
    def __init__(self, Title: str, NumberOfPages: int):
        self.Title = Title
        self.NumberOfPages = NumberOfPages

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class PrintQueue:
    def __init__(self):
        self.top = None
        self.last = None
        self.size = 0

    def enqueue(self, item):
        if self.top is None:
            self.top = Node(item)
            self.last = self.top

        else:
            new_last = Node(item, None)
            self.last.next = new_last
            self.last = new_last

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.top.value
        self.top = self.top.next
        self.size -=1
        return value

    def is_empty(self):
        return self.size == 0

    def count(self):
        return self.size
