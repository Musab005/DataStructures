from src.lists import list
from src.linkedlists import linked_list


class Map:

    # Creates the internal dynamic array (buckets) of a certain size.
    def __init__(self):
        self.size = 10
        self.buckets = list.List(self.size)

    # TODO: learn hashing algorithms
    # A private method that takes a key and returns an index (e.g., hash(key) % self.size).
    def _hash(self, key):
        hashed_value = hash(key)
        dest_index = hashed_value % self.size
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
        # update value if key exists or append new (key, value)
        else:
            for pair in curr_linked_list:
                if pair[0] == key:
                    pair[1] = value
                    return
            curr_linked_list.append([key, value])

    # Hashes the key to find the bucket. Searches the Linked List in that bucket for the key
    # and returns its value. If not found, raise a KeyError.
    def __getitem__(self, key):
        dest_index = self._hash(key)
        curr_linked_list = self.buckets.array[dest_index]
        if not curr_linked_list:
            raise KeyError
        for pair in curr_linked_list:
            if pair[0] == key:
                return pair[1]
        raise KeyError

    # Hashes the key, finds the bucket, and uses your LinkedList.remove_by_value to remove the (key, value)
    # pair.
    def remove(self, key):
        dest_index = self._hash(key)
        curr_linked_list = self.buckets.array[dest_index]
        if not curr_linked_list:
            raise KeyError
        for pair in curr_linked_list:
            if pair[0] == key:
                curr_linked_list.remove_by_value(pair)
                return
        raise KeyError

    # TODO: learn diff between __del__, __delitem__, del map[key], remove(key).
    def __del__(self):
        pass

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
