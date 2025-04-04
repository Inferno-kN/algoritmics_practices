class List:
    def __init__(self, size):
        self.__lst = []
        self.__size = size

    def append(self, value):
        self.__lst.append(value)

    def pop(self, index):
        return self.__lst.pop(index)

    def remove(self, value):
        if value not in self.__lst:
            raise ValueError
        else:
            self.__lst.remove(value)

    def size(self):
        return self.__size

    def insert(self, value, index):
        self.__lst.insert(index, value)


    def __str__(self):
        return self.__lst
