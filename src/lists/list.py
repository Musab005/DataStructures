# Implement list (dynamic array)

# Time complexity:
# 1) Access/search (by index) - arr[i] = O(1)
# 2) Append - list.append(x) = O(1) amortized
# When there’s free space, appending is constant time.
# If the array is full, Python allocates a bigger block (1.125x – 2x growth factor),
# then copies all elements over → O(n) for that operation. But since resizing doesn’t happen every time,
# the average cost per append is still O(1).
# 4) Insert at beginning or middle - list.insert(0, x) or list.insert(i, x) = O(n) because
# all subsequent elements must shift one position to the right.
# 5) Pop from end - list.pop() = O(1) as it just reduces the array size by 1, no shifting.
# 6) Pop from beginning or middle - list.pop(i) = O(n) as all subsequent elements shift left.
# 7) Search by value - arr.index(40) or '40 in arr' = O(n) bcs its a linear scan

class List:
    def __init__(self, size):
        self.size = size  # total capacity available
        self.length = 0  # actual elements stored
        self.array = [None] * size

    def append(self, value):
        if self.length >= self.size:
            # increase size
            self.size = 2 * self.size
            # copy old elements
            new_array = [None] * self.size
            for i in range(0, len(self.array)):
                new_array[i] = self.array[i]
            self.array = new_array

        # insert
        self.array[self.length] = value
        self.length += 1

    def pop(self, index=None):
        value = self.array[index]
        # if index given and is not the last index
        if index and index != self.length - 1:
            i = index
            while i + 1 <= self.size - 1:
                self.array[i] = self.array[i + 1]
                i += 1
            self.array[self.length - 1] = None
            return value
        else:  # pop from end
            self.array[self.length - 1] = None
            self.length -= 1
            return value

    def insert(self, index, value):
        if self.length >= self.size:
            # increase size
            self.size = 2 * self.size
            # copy old elements
            new_array = [None] * self.size
            for i in range(0, self.length):
                new_array[i] = self.array[i]
            self.array = new_array

        for i in range(self.length - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = value

    def delete(self, value):
        for i in range(0, self.size):
            if self.array[i] == value:
                # edge case - last index
                if i == self.size - 1:
                    self.array[i] = None
                    return 0

                # normal flow
                while i + 1 < self.size:
                    self.array[i] = self.array[i + 1]
                    i += 1
                return 0

    # returns the first index given a value
    def index(self, value):
        for i in range(0, self.size):
            if self.array[i] == value:
                return i
        return -1

    # get value at the specified index
    def get(self, index):
        return self.array[index]
