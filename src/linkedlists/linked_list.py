class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        # comparing value of nodes, not the next connection
        # allows use of ==
        def __eq__(self, other):
            if isinstance(other, LinkedList.Node):
                if other.value == self.value:
                    return True
            return False

    class _Iterator:
        def __init__(self, head_node):
            # The iterator's only state is the node it's currently looking at.
            self.current_node = head_node

        def __iter__(self):
            # The iterator is already an iterator, so it just returns itself.
            return self

        def __next__(self):
            # This is the O(1) magic. No loops, no get_at.
            if not self.current_node:
                # We've walked off the end of the list.
                raise StopIteration
            # Grab the value before we move on.
            value_to_return = self.current_node.value
            # Move our finger to the next node for the next call.
            self.current_node = self.current_node.next
            return value_to_return

    # Adds a new node to the beginning of the list.
    def prepend(self, value):
        new_node = self.Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        return

    # Adds a new node to the end of the list.
    # O(1) with tail node present, O(n) otherwise
    def append(self, value):
        new_node = self.Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return

    # Removes and returns the data from the head of the list.
    def remove_first(self):
        # length = 0
        if self.size == 0:
            return
        # length >= 1
        else:
            # length == 1
            if self.size == 1:
                temp = self.head
                self.head = None
                self.tail = None
                self.size -= 1
                return temp.value
            else:
                # length > 1
                temp = self.head
                self.head = self.head.next
                self.size -= 1
                return temp.value

    # Removes and returns the data from the tail of the list.
    def remove_last(self):
        # length = 0
        if self.size == 0:
            return
        # length = 1
        elif self.size == 1:
            self.head = None
            value = self.tail.value
            self.tail = None
            self.size -= 1
            return value
        # length > 1
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            value = self.tail.value
            self.tail = temp
            self.size -= 1
            return value

    # Finds the first node with the given data and removes it.
    def remove_by_value(self, value):
        # length = 0
        if self.size == 0:
            return
        # length = 1
        elif self.size == 1:
            if self.head.value == value:
                self.head = None
                self.tail = None
                self.size -= 1
                return
        # length > 1
        else:
            prev = self.head
            # edge case: head needs to be removed
            if prev.value == value:
                self.head = prev.next
                return
            else:
                curr = self.head.next
                while curr:
                    if curr.value == value:
                        prev.next = curr.next
                        self.size -= 1
                        return
                    prev = curr
                    curr = curr.next
                return

    # Returns the first node containing the given data, or None if not found.
    def search(self, value):
        # length = 0
        if not self.head:
            return None
        # length >= 1
        else:
            temp = self.head
            while temp:
                if temp.value == value:
                    return temp
                temp = temp.next

    # Returns True if the list is empty.
    def is_empty(self):
        return self.size == 0

    # Returns the number of nodes in the list.
    def get_size(self):  # or __len__
        return self.size

    # Returns a string representation of the list, i.e. allows str(list)
    def __str__(self):
        if self.size > 0:
            temp = self.head
            out_list = []
            while temp:
                out_list.append(str(temp.value))
                temp = temp.next
            return ' -> '.join(out_list) + " -> None"
        else:
            return "None"

    # Reverses the list in-place. Iterative implementation
    def reverse(self):
        if self.size > 1:
            # length >= 2
            prev_node = None
            curr_node = self.head
            while curr_node:
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
            self.head = prev_node

    # recursive implementation
    def reverse_2(self):
        if self.size > 1:
            self.head = self.reverse_recurse(self.head)

    def reverse_recurse(self, head):
        # The Base Case: What is the absolute simplest list I could be asked to reverse?
        if not head.next:
            return head
        # My One Job: If I assume a magical function has already reversed the rest of the list for me,
        # what is the one tiny piece of work I need to do to finish the job?
        # Recursive Leap of Faith: reverse(B) below will return a reversed list with new head pointing to the tail
        # How would you switch A and B pointers?
        new_head = self.reverse_recurse(head.next)
        head.next.next = head
        head.next = None
        return new_head

    # Finds the middle node of the list using the "fast and slow pointer" technique.
    def find_middle(self):
        if self.size == 0:
            return
        elif self.size == 1:
            return self.head.value
        else:
            # length >= 2
            slow = self.head
            fast = self.head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow.value

    # Inserts a new node at a specific position. If index out of bounds, append at the end
    def insert_at(self, index, data):
        # empty list
        if self.size == 0:
            new_node = self.Node(data)
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        # index = last or out of bounds, append at end
        elif index >= self.size:
            self.append(data)
            return
        # normal flow
        else:
            if index == 0:
                self.prepend(data)
            else:
                count = 0
                temp = self.head
                # loop ends when count = index-1. List wouldn't end since we ensured (index <  size) above
                while count < index - 1:
                    temp = temp.next
                    count += 1
                # temp is the node before the index to be inserted
                next_node = temp.next
                temp.next = self.Node(data)
                temp.next.next = next_node
                self.size += 1
                return

    # Retrieves the data at a specific position.
    def get_at(self, index):
        if self.size == 0 or index >= self.size:
            raise IndexError
        count = 0
        temp = self.head
        # index is valid as checked at the beginning
        while count < index:
            temp = temp.next
            count += 1
        return temp.value

    # allows use of len(list)
    def __len__(self):
        return self.size

    # allows use of it = iter(list) -> returns an iterator object that can be given as argument to the method next(it)
    def __iter__(self):
        # Whenever a for loop starts, this __iter__ method is called, and it creates a NEW iterator object.
        return self._Iterator(self.head)




