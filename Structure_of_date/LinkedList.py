class Node:

    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.first_node = None
        self.last_node = None

    def count(self):
        count = 0

        current_node = self.first_node
        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def append(self, value):
        if self.first_node is None:
            self.first_node = Node(value, None)
            return

        current_node = self.first_node
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = Node(value, None)

    def append_first(self, value):
        node = Node(value, self.first_node)
        self.first_node = node


    def pop(self, index):
        if index == 0:
            value = self.first_node.value
            self.first_node = self.first_node.next
            return value

        current_index = 0
        prev = self.first_node
        while current_index != index - 1:
            current_index += 1
            prev = prev.next

        value = prev.next.value
        prev.next = prev.next.next
        return value


l = LinkedList()
print(l.count())
l.append(10)
print(l.count())
l.append(20)
print(l.count())
print(l.pop(0))
print(l.count())

