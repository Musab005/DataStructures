# Implement list (dynamic array)

class List:
    def __init__(self, size=10):
        self.size = size  # total capacity available
        self.length = 0  # actual elements stored
        self.array = [None] * size

    def append(self, value):
        # before appending, if already at full capacity
        if self.length >= self.size:
            self._increase_size()
        # insert at end which has the index equal to the value of self.length
        self.array[self.length] = value
        self.length += 1
        return

    # insert value at index
    def insert(self, index, value):
        # before insertion, if already at full capacity
        if self.length >= self.size:
            self._increase_size()
        # reversed for loop. i starts at the last element index, ends at i = index (inclusive)
        # shift all elements to the right including the element at index
        for i in range(self.length - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        # insert at index
        self.array[index] = value
        self.length += 1
        return

    # remove first occurrence of value, raise valueError otherwise
    def remove(self, value):
        found_index = -1
        for i in range(self.length):
            if self.array[i] == value:
                found_index = i
                break

        if found_index == -1:
            raise ValueError(f"list.remove{value}: value not in list")

        self._remove_and_shift_left(found_index)

    # remove element from an index and return it
    def pop(self, index=None):
        if self.length == 0:
            raise IndexError("pop from empty list")

        # Determine the actual index to pop
        pop_index = index
        if pop_index is None:
            pop_index = self.length - 1  # Default to the last element

        # Validate the index
        if not (0 <= pop_index < self.length):
            raise IndexError("pop index out of range")

        # Get the value and perform the removal
        value = self.array[pop_index]
        self._remove_and_shift_left(pop_index)
        return value

    # clear all elements
    def clear(self):
        self.array = [None] * self.size
        self.length = 0

    # returns the index for the first occurrence of a value
    # optional arguments start and end: x[, start[, end]] to limit search to a subsequence
    # always return index 0-based
    def index(self, x, start=None, end=None):
        if start:
            if end:
                return self._search_value(start, end, x)
            else:
                return self._search_value(start, self.length, x)
        else:
            return self._search_value(0, self.length, x)

    # return number of occurrences of a value
    def count(self, x):
        count = 0
        for i in range(0, self.length):
            if self.array[i] == x:
                count += 1
        return count

    # TODO: sort in place
    def sort(self, *, key=None, reverse=False):
        if self.length > 1:
            self._insertion_sort(key=key, reverse=reverse)

    # reverse in place
    # '//' rounds down the quotient
    def reverse(self):
        midpoint = self.length // 2
        # works for both even and odd
        for i in range(0, midpoint):
            temp = self.array[i]
            self.array[i] = self.array[self.length - 1 - i]
            self.array[self.length - 1 - i] = temp

    def copy(self):
        new_list = List(self.size)
        for i in range(self.length):
            new_list.append(self.array[i])
        return new_list

    def _increase_size(self):
        # double the size (capacity)
        self.size = 2 * self.size
        # copy old elements into the new bigger array
        new_array = [None] * self.size
        for i in range(0, self.length):
            new_array[i] = self.array[i]
        # assign the new array to the object
        self.array = new_array

    # helper function to find the index of a value
    def _search_value(self, start, end, value):
        for i in range(start, end):
            if self.array[i] == value:
                return i
        raise ValueError

    def _remove_and_shift_left(self, index):
        # shift all elements to left
        # loop will start from left (from index)
        # will end at second last element
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        # remove last element
        self.array[self.length - 1] = None
        self.length -= 1
        return

    # O(n^2) by scanning and finding lowest, replacing it at the beginning
    def _selection_sort(self, *, key=None, reverse=False):
        for i in range(self.length):
            # minimum element seen in the subsequence starting from i
            min_element = self.array[i]
            min_index = i
            # scan the entire subsequence starting from i
            for y in range(i, self.length):
                if self.array[y] < min_element:
                    min_element = self.array[y]
                    min_index = y
            # swap the minimum element with element at index i
            temp = self.array[i]
            self.array[i] = min_element
            self.array[min_index] = temp
        if reverse:
            self.reverse()

    # O(n^2) by swapping pairs
    def _bubble_sort(self, *, key=None, reverse=False):
        for i in range(self.length):
            for y in range(self.length - 1):
                if self.array[y] > self.array[y + 1]:
                    temp = self.array[y]
                    self.array[y] = self.array[y + 1]
                    self.array[y + 1] = temp
        if reverse:
            self.reverse()

    # O(n^2) by maintaining a sorted array
    def _insertion_sort(self, *, key=None, reverse=False):
        sorted_array = List(self.size)
        sorted_array.append(self.array[0])
        for i in range(1, self.length):
            curr = self.array[i]
            shifted = False
            for y in range(len(sorted_array)):
                if curr < sorted_array[y]:
                    shifted = True
                    # shift right
                    for z in range(len(sorted_array) - 1, y - 1, -1):
                        sorted_array.insert(z+1, sorted_array[z])
                    # set new value
                    sorted_array[y] = curr
                    break
            if not shifted:
                sorted_array.append(curr)
        self.array = sorted_array
        if reverse:
            self.reverse()

    # for printing
    def __str__(self):
        if self.length == 0:
            return "[]"
        items = [str(self.array[i]) for i in range(self.length)]
        return f"[{', '.join(items)}]"

    # allows len(my_list)
    def __len__(self):
        return self.length

    # allows bracket notation like my_list[3]
    def __getitem__(self, index):
        if index < 0:
            index += self.length
        if not (0 <= index < self.length):
            raise IndexError("list index out of range")
        return self.array[index]

    # Allows my_list[3] = "new_value".
    def __setitem__(self, index, value):
        if index < 0:
            index += self.length
        if not 0 <= index < self.length:
            raise IndexError("list assignment index out of range")
        self.array[index] = value

    # allows the use of "=="
    # object on left calls its dunder method (is represented by "self")
    def __eq__(self, other):
        if isinstance(other, List) or isinstance(other, list):
            if len(other) == self.length:
                for i in range(self.length):
                    if self.array[i] != other[i]:
                        return False
                return True

        return False
