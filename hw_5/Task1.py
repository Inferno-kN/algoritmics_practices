class Node:
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev

class Stack: #операции is_empty, peek, size, pop, push
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def get_size(self):
        return self.size

    def peek(self):
        if self.is_empty():
            return
        return self.top.value

    def pop(self):
        if self.is_empty():
            return None

        value = self.top.value
        self.top = self.top.prev
        self.size -= 1
        return value


    def push(self, value):
        node = Node(value, None)
        if self.top is None:
            self.top = node
        else:
            node.prev = self.top
            self.top = node

        self.size += 1




st = Stack()
st.push(4)
st.push(3)
st.push(5)
print(st.pop())
print(st.pop())
print(st.peek())
print(st.get_size())
print(st.pop())
print(st.peek())





