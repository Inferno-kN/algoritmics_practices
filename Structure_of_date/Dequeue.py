class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Dequeue:

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def peek_front(self):
        if self.is_empty():
            return None
        return self.front.value

    def peek_back(self):
        if self.is_empty():
            return None
        return self.back.value


    def append_front(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            new_node.next = self.front #типа если сама очередь(дэка) не пустая, то мы ВРОДЕ КАК создаем новый нод перед текущим спереди нодом
            self.front.prev = new_node # а здесь и на строчку ниже, я обновил ссылки на ноды
            self.front = new_node

        self.size += 1 #но мне кажется реализация плохая

    def append_back(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            new_node.prev = self.back #здесь тоже самое как в append_front но наоборот, ток мы создаем нод после текущего заднего нода
            self.back.next = new_node
            self.back = new_node

        self.size += 1 #но мне кажется реализация плохая

    def remove_front(self):
        if self.is_empty():
            return None

        value = self.front.value
        self.front = self.front.next
        if self.front is not None:
            self.front.prev = None

        self.size -= 1
        return value

    def remove_back(self):
        if self.is_empty():
            return None

        value = self.back.value
        self.back = self.back.prev
        if self.back is not None:
            self.back.next = None

        self.size -= 1
        return value

    def size(self):
        return self.size

    def insert(self, index, item):
        if index < 0 or index > self.size:
            raise IndexError("Индекс находится вне диапазона")

        new_node = Node(item)

        if index == 0:
            self.append_front(item)
        elif index == self.size:
            self.append_back(item)
        else:
            current_node = self.front
            count = 0
            while count < index:
                current_node = current_node.next
                count += 1

            new_node.prev = current_node.prev
            new_node.next = current_node

            if current_node.prev is not None:
                current_node.prev.next = new_node

            current_node.prev = new_node

            if index == 1:
                self.front = new_node

            self.size += 1


dq = Dequeue()
dq.append_back(3)
dq.append_back(2)
dq.append_front(5)
print(dq.peek_back())
print(dq.peek_front())
dq.insert(2, 4)
print(dq.remove_front())
print(dq.remove_back())
print(dq.size)


