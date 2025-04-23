def malloc(size):
    result = []
    for i in range(size):
        result.append([])
    return result


def my_hash(key):
    return len(key)

class HashTableNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self, size):
        self.memory = malloc(size)
        self.size = size
        self.count = 0


    def calculate_index(self, key):
        return my_hash(key) % self.size

    def get_count(self): return self.count

    def __check_rehash(self):
        if self.count / self.size >= 0.75:
            new_size = self.size * 2 + 1
            self.__rehash(new_size)


    def __rehash(self, new_size):
        new_memory = malloc(new_size)

        for i, elem in enumerate(self.memory):
            new_memory[i] = elem

        self.size = new_size
        self.memory = new_memory

    def get(self, key):
        index = self.calculate_index(key)

        if len(self.memory[index]) > 0:
            for node in self.memory[index]:
                if node.key == key:
                    return node.value
            return None


    def set(self, key, value):
        self.__check_rehash()
        index = self.calculate_index(key)
        if len(self.memory[index]) == 0:
            self.memory[index].append(HashTableNode(key, value))
            self.count += 1
        else:
            found_index = -1
            for i in range(len(self.memory[index])):
                if self.memory[index][i].key == key:
                    found_index = i

            if found_index == -1:
                self.memory[index].append(HashTableNode(key, value))
                self.count += 1
            else:
                self.memory[index][found_index].value = value

    def contains(self, key):
        return self.get(key) is not None


    def remove(self, key):
        index = self.calculate_index(key)
        for i in range(len(self.memory[index])):
            if self.memory[index][i].key == key:
                result = self.memory[index].pop(i)
                self.count -= 1
                return result.value
        return None




ht = HashTable(12)

ht.set("doodle", 3)
ht.set("jump", 5)
ht.set("return", 8)

print(ht.get("jump"))

