from ctypes import create_unicode_buffer
from logging import currentframe
from os.path import curdir


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.first_node = None

    def front_append(self, value):
        if self.first_node is None:
            self.first_node = Node(value)
        else:
            new_node = Node(value, self.first_node)
            self.first_node = new_node

    def back_append(self, value):
        if self.first_node is None:
            self.first_node = Node(value)
        else:
            current_node = self.first_node
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def size(self):
        count = 0
        current_node = self.first_node
        while current_node is not None:
            current_node = current_node.next
            count += 1

        return count

    def get(self, index):
        if index < 0:
            raise IndexError

        count = 0

        current_node = self.first_node
        while count != index:
            current_node = current_node.next
            count += 1

        if current_node is None:
            raise IndexError

        return current_node.value

    def set(self, index, value):
        count = 0

        current_node = self.first_node
        while current_node is not None and count != index:
            current_node = current_node.next
            count += 1
        current_node.value = value


    def reverse(self):

        reverse_list = LinkedList()

        current_node = self.first_node
        while current_node.next is not None:
            reverse_list.front_append(current_node.value)
            current_node = current_node.next

        self.first_node = reverse_list.first_node


    def front_remove(self):
        self.first_node = self.first_node.next


    def back_remove(self):
        current_node = self.first_node
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = None


    def remove(self, index):
        if index == 0:
            self.front_remove()

        else:
            current_node = self.first_node
            count = 0

            while count != index - 1:
                current_node = current_node.next
                count += 1

            current_node.next = current_node.next.next

a = LinkedList()
print(a.size())
a.back_append(3)
print(a.size())
print(a.get(0))
a.back_append(5)
print(a.size())
a.remove(1)
print(a.size())