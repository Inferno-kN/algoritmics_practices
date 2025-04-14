class AvengersMission:
    def __init__(self, description: str, priority: int):
        self.description = description
        self.priority = priority
        self.next = None

class AvengersPriorityQueue:
    def __init__(self):
        self.first_node = None
        self.size = 0

    def dequeue(self, description, priority):
        node = AvengersMission(description, priority)

        if self.first_node is None or self.first_node.priority > priority:
            node.next = self.first_node
        else:
            current = self.first_node
            while current.next is not None and current.next.priority <= priority:
                current = current.next
            node.next = current.next
            current.next = node

    def is_empty(self):
        return self.size == 0

    def count(self):
        return self.size

    def peek(self):
        if self.is_empty():
            return None
        return self.first_node.priority
