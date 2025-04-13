class Node:

    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class DoubleLinkedList:

    def __init__(self):
        self.first_node = None
        self.last_node = None

    def push_front(self, value):
        if self.first_node is None:
            self.first_node = Node(value, None, None)
            return

        new_first_node = Node(value, self.first_node, None)
        self.first_node.prev = new_first_node
        self.first_node = new_first_node


    def push_back(self, value):
        if self.first_node is None:
            self.first_node = Node(value, None, None)
            return

        current_node = self.first_node

        while current_node.next is not None:
            current_node = current_node.next

        last_node = Node(value, None, current_node)
        current_node.next = last_node

    def length(self):

        if self.first_node is None:
            return 0

        length = 0

        current_node = self.first_node

        while current_node is not None:

            length += 1
            current_node = current_node.next

        return length

    def insert(self, value, index):
        counter = 0
        current_node = self.first_node
        while counter != index:
            counter += 1
            current_node = current_node.next
        new_node = Node(value, current_node, current_node.prev)
        buffer_node = current_node.prev
        current_node.prev = new_node
        buffer_node.next = new_node


    def __str__(self):
        if self.first_node is None:
            return ""
        result = ""

        current_node = self.first_node

        while current_node is not None:
            result += str(current_node.value)

            if current_node.next is not None:
                result += " "
            current_node = current_node.next

        return result

    def remove(self, index):
        current_node = self.first_node
        count = 0

        while count != index:
            count += 1
            current_node = current_node.next

        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev

    def remove_front(self):
        if self.first_node is None:
            return

        if self.first_node == self.last_node:
            self.first_node = None
            self.last_node = None
        else:
            self.first_node = self.first_node.next
            self.first_node.prev = None

    def remove_back(self):
        if self.last_node is None:
            return

        if self.first_node == self.last_node:
            self.first_node = None
            self.last_node = None
        else:
            self.last_node = self.last_node.prev
            self.last_node.next = None



    def size(self):
        return self.length()


l = DoubleLinkedList()
l.push_front(4)
l.push_back(3)
l.push_back(2)
l.push_back(5)
l.insert(1, 3)
print(l.length())
print(l)
l.remove(2)
print(l)



