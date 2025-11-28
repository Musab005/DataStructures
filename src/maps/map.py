from src.lists import list
from src.linkedlists import linked_list


class Map:

    # Creates the internal dynamic array (buckets) of a certain size.
    def __init__(self, size=10):
        self.count = 0
        self.size = size
        self.buckets = list.List(self.size)

    # A private method that takes a key and returns an index (e.g., hash(key) % self.size).
    def _hash(self, key):
        hashed_value = hash(key)
        dest_index = hashed_value % self.sizeRm
        return dest_index

    # Hashes the given key to find the bucket index. If the bucket is empty, create a new
    # Linked List there. Search the Linked List in that bucket for the key. If it exists, update the value.
    # If it doesn't, append a new (key, value) pair to the Linked List.
    def __setitem__(self, key, value):
        dest_index = self._hash(key)
        curr_linked_list = self.buckets.array[dest_index]

        # bucket is empty
        if not curr_linked_list:
            new_linked_list = linked_list.LinkedList()
            new_linked_list.append([key, value])
            self.buckets.array[dest_index] = new_linked_list
            self.count += 1
        # update value if key exists or append new (key, value)
        else:
            for pair in curr_linked_list:
                if pair[0] == key:
                    pair[1] = value
                    return
            curr_linked_list.append([key, value])
            self.count += 1

    # Hashes the key to find the bucket. Searches the Linked List in that bucket for the key
    # and returns its value. If not found, raise a KeyError.
    def __getitem__(self, key):
        dest_index = self._hash(key)
        curr_linked_list = self.buckets.array[dest_index]
        if self.count == 0:
            raise KeyError
        for pair in curr_linked_list:
            if pair[0] == key:
                return pair[1]
        raise KeyError

    # Hashes the key, finds the bucket, and uses LinkedList.remove_by_value to remove the (key, value) pair. Ideally
    # need to be more efficient by writing a remove key value pair by key method in linked list because rn it loops
    # to find key and then remove_by_value searches the entire linked list again for the key value pair!
    def remove(self, key):
        dest_index = self._hash(key)
        curr_linked_list = self.buckets.array[dest_index]
        if self.count == 0:
            raise KeyError
        for pair in curr_linked_list:
            if pair[0] == key:
                curr_linked_list.remove_by_value(pair)
                self.count -= 1
                return
        raise KeyError

    # Returns a string representation of the HashMap for printing.
    def __str__(self):
        map_str = ""
        for i in range(len(self.buckets.array)):
            map_str += f"index {i}: "
            if self.buckets.array[i]:
                for pair in self.buckets.array[i]:
                    map_str += f"{pair} "
            else:
                map_str += "Empty"
            map_str += "\n"

        return map_str

    # returns the total number of key-value pairs stored in the map
    def __len__(self):
        return self.count

    # Remove this item (key value pair) from the map
    def __delitem__(self, key):
        self.remove(key)

    # Return True if key exists, false otherwise
    def __contains__(self, key):
        dest_index = self._hash(key)
        curr_linked_list = self.buckets.array[dest_index]
        # using 'not curr_linked_list' here and not in other methods because of an edge case
        # if a key is not in the map, the contains method still hashes it and finds the suitable
        # dest index. However, the list at that index can be None but the count of the map can be > 0.
        if not curr_linked_list or self.count == 0:
            return False
        for pair in curr_linked_list:
            if pair[0] == key:
                return True
        return False



