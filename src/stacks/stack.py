from src.linkedlists.linked_list import LinkedList


class Stack:

    def __init__(self):
        self.items = LinkedList()

    def push(self, item):
        self.items.prepend(item)

    def pop(self):
        self.items.remove_first()

    def peek(self):
        return self.items.get_at(0)

    def is_empty(self):
        return self.items.is_empty()

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

