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
        for i in range(0, self.size):
            if self.array[i] == value:
                # edge case = value to remove is at the last index in the array
                if i == self.size - 1:
                    self.array[i] = None
                    self.length -= 1
                    return

                # value to remove is anywhere but the last index
                # shift all elements to the left by first replacing the value to remove (at index i)
                while i + 1 < self.size:
                    self.array[i] = self.array[i + 1]
                    i += 1
                # remove the last value
                self.array[self.length - 1] = None
                self.length -= 1
                return

        raise ValueError

    # remove element from an index and return it
    def pop(self, index=None):
        # if list is empty or index is out of range
        if self.length == 0 or index > self.length - 1:
            raise IndexError

        # if index given and is not the last index
        if index and index != self.length - 1:
            value = self.array[index]
            i = index
            # loop from the index to the right (until i+1 reaches the rightmost element)
            # doing this way because the array might end at the last legal value with no empty cells remaining
            # shift all elements to the left
            while i + 1 < self.length:
                self.array[i] = self.array[i + 1]
                i += 1
            self.array[self.length - 1] = None
            self.length -= 1
            return value

        # if index not given or is the last index
        else:
            value = self.array[index]
            self.array[self.length - 1] = None
            self.length -= 1
            return value

    # remove all elements
    def clear(self):
        for i in range(0, self.length):
            self.pop()

    # returns the index for the first occurrence of a value
    # optional arguments start and end: x[, start[, end]] to limit search to a subsequence
    # always return index 0-based
    def index(self, x, start=None, end=None):
        if start:
            if end:
                self._search_value(start, end, x)
            else:
                self._search_value(start, self.length, x)
        else:
            self._search_value(0, self.length, x)
        raise ValueError

    # return number of occurrences of a value
    def count(self, x):
        count = 0
        for i in range(0, self.length):
            if self.array[i] == x:
                count += 1
        return count

    # TODO: sort in place
    def sort(self, *, key=None, reverse=False):
        pass

    # reverse in place
    def reverse(self):
        midpoint = self.length // 2
        for i in range(0, midpoint):
            temp = self.array[i]
            self.array[i] = self.array[self.length - 1 - i]
            self.array[self.length - 1 - i] = temp

    # TODO: returns shallow copy
    def copy(self):
        return [[i] for i in self.array]

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
