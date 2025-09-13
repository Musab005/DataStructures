class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    # Adds a new node to the beginning of the list.
    def prepend(self, value):
        self.size += 1
        new_node = self.Node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Adds a new node to the end of the list.
    def append(self, value):
        self.size += 1
        new_node = self.Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            # at this point temp.next is None
            temp.next = new_node

    # Removes and returns the data from the head of the list.
    def remove_first(self):
        # length = 0
        if not self.head:
            return
        # length >= 1
        else:
            temp = self.head
            # if length = 1 then self.head = None otherwise self.head = second node in list
            self.head = self.head.next
            self.size -= 1
            return temp

    # Removes and returns the data from the tail of the list.
    def remove_last(self):
        # length = 0
        if not self.head:
            return
        # length >= 1
        else:
            temp = self.head
            # if length = 1
            if not temp.next:
                self.head = None
                self.size -= 1
                return temp
            # length > 1
            while temp.next.next:
                temp = temp.next
            # at this point temp.next.next is None
            # i.e. temp is the second last node in the list
            curr = temp.next
            temp.next = None
            self.size -= 1
            return curr

    # Finds the first node with the given data and removes it.
    def remove_by_value(self, value):
        # length = 0
        if not self.head:
            return
        # length >= 1
        else:
            # if length = 1
            if not self.head.next:
                if self.head.value == value:
                    self.head = None
                    self.size -= 1
                return
            # length > 1
            pointer1 = self.head
            while pointer1.next:
                pointer2 = pointer1.next
                if pointer2.value == value:
                    pointer1.next = pointer2.next
                    self.size -= 1
                    return
                pointer1 = pointer1.next
            return

    # Returns the first node containing the given data, or None if not found.
    def search(self, value):
        # length = 0
        if not self.head:
            return None
        # length >= 1
        else:
            # if length = 1
            if not self.head.next:
                if self.head.value == value:
                    temp = self.head
                    self.head = None
                    return temp
                else:
                    return None
            # length > 1
            pointer1 = self.head
            while pointer1.next:
                pointer2 = pointer1.next
                if pointer2.value == value:
                    pointer1.next = pointer2.next
                    return pointer2
                pointer1 = pointer1.next
            return None

    # Returns True if the list is empty.
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    # Returns the number of nodes in the list.
    def get_size(self):  # or __len__
        return self.size

    # Returns a string representation of the list, i.e. allows str(list)
    def __str__(self):
        if self.size > 0:
            temp = self.head
            out_list = ' '
            temp_str = out_list.join([f'{temp.value}', '->'])
            while temp.next:
                temp = temp.next
                temp_str = out_list.join([temp_str, f'{temp.value}', '->'])
            temp_str = out_list.join([temp_str, 'None'])
            return temp_str
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

    # Inserts a new node at a specific position.
    def insert_at(self, index, data):
        pass

    # Retrieves the data at a specific position.
    def get_at(self, index):
        count = 0
        temp = self.head
        while count < index and temp.next:
            temp = temp.next
            count += 1
        # loop breaks if index reached or index doesn't exist
        if count != index:
            raise IndexError
        return temp.value
