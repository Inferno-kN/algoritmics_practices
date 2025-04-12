class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class Priority: #операции: put, get, is_empty, peek, size
    def __init__(self):
        self.first_node = None
        self.size = 0

    def put(self, value, priority):
        new_node = Node(value, priority)

        if self.first_node is None:
            new_node.next = self.first_node
            self.first_node = new_node
        else:
            current_node = self.first_node
            while current_node.next is not None and current_node.next.priority <= priority:
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

        self.size += 1



    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def get_priority(self): # извлекаем элемент с высшим приоритетом
        if self.is_empty():
            return None

        value = self.first_node.value
        self.first_node = self.first_node.next
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.first_node.value

