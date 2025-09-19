from src.linkedlists.linked_list import LinkedList


class Queue:

    def __init__(self):
        self.items = LinkedList()

    # Adds an item to the back of the queue.
    # O(1) since we have the tail pointer
    def enqueue(self, item):
        self.items.append(item)

    # Removes and returns the front item.
    # O(1) since we just move self.head
    def dequeue(self):
        return self.items.remove_first()

    # Returns the front item without removing it.
    # O(1) since we just check self.head's value
    def front(self):
        if self.items.head is not None:
            return self.items.head.value
        else:
            return None

    # Returns True if the queue is empty.
    # O(1) since we just check self.size
    def is_empty(self):
        return self.items.is_empty()

    # Returns the number of items.
    # O(1) since we just return self.size
    def __len__(self):
        return len(self.items)

    # O(n) since we traverse the list
    def __str__(self):
        return str(self.items)
