class Stack:
    def __init__(self):
        self.date = []

    def push(self, element):
        self.date.append(element)

    def pop(self):
        return self.date.pop()

    def top(self):
        return self.date[-1]

    def is_empty(self):
        return len(self.date) == 0

    def __str__(self):
        return