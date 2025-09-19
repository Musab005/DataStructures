from src.linkedlists.linked_list import LinkedList


class Stack:

    def __init__(self):
        self.items = LinkedList()

    # Adds an item to the top.
    # O(1) since we just shift self.head
    def push(self, item):
        self.items.prepend(item)

    # Removes and returns the top item.
    # O(1) since we just shift self.head
    def pop(self):
        self.items.remove_first()

    # Returns the top item without removing it.
    # O(1) since we just check self.head's value
    def peek(self):
        if self.items.head is not None:
            return self.items.head.value
        else:
            return

    # O(1) since we just check self.size
    def is_empty(self):
        return self.items.is_empty()

    # O(1) since we just check self.size
    def __len__(self):
        return len(self.items)

    # O(n) since we traverse the list
    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

