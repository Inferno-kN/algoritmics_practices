class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:

    def __init__(self):
        self.first_node = None


    def is_empty(self):
        return self.first_node is None

    def push(self, value):
        new_node = Node(value, self.first_node)
        self.first_node = new_node

    def pop(self):
        if self.is_empty():
            return None

        value = self.first_node.value
        self.first_node = self.first_node.next
        return value

    def peek(self):
        if self.is_empty():
            return

        return self.first_node.value

    def size(self):
        return self.size

st = Stack()
st.push(5)
st.push(3)
st.push(4)
print(st.pop())
print(st.pop())
print(st.peek())
print(st.pop())


