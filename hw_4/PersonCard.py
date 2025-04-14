class PersonCard:

    def __init__(self, name: str, age: int, occupation: str):
        self.name = name
        self.age = age
        self.occupation = occupation

class Node:
    def __init__(self, person: PersonCard):
        self.person = person
        self.next = None

class PersonList:
    def __init__(self):
        self.count = 0
        self.head = None


    def add_person(self, person: PersonCard):
        new_node = Node(person)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def append_person(self, person: PersonCard):
        new_node = Node(person)
        if self.count == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.count += 1


    def insert_person_at(self, index: int, person: PersonCard):
        new_node = Node(person)
        if index < 1 or index > self.count:
            raise IndexError

        current_node = self.head
        for _ in range(index - 1):
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
        self.count += 1

    def remove_first_person(self):
        person = self.head.person
        self.head = self.head.next
        self.count -= 1
        return person

    def remove_last_person(self):
        if not self.head:
            raise ValueError("Список пустой")
        elif self.head.next is None:
            removed_person = self.head.person
            self.head = None
            self.count -= 1
            return removed_person

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        removed_person = current_node.next.person
        current_node.next = None
        self.count -= 1
        return removed_person

    def remove_person(self, person: PersonCard):
        if not self.head:
            raise ValueError("Список пуст")

        elif self.head.person == person:
            return self.remove_first_person()

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.person == person:
                current_node.next = current_node.next.next
                self.count -= 1
                return person
            current_node = current_node.next
        raise ValueError(f"{person} нет в списке")

    def clear_all(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head == 0

    def total_people(self):
        return self.count




