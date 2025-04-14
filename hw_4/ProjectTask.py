from datetime import datetime

class ProjectTask:
    def __init__(self, description: str, date: datetime):
        self.description = description
        self.date = date

class TaskStack:
    def __init__(self):
        self.stack = []

    def push(self, task: ProjectTask):
        self.stack.append(task)

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def count(self)-> int:
        return len(self.stack)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None