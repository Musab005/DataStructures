from src.lists import list
from src.linkedlists import linked_list


class Map:
    def __init__(self):
        self.size = 10
        self.buckets = list.List(self.size)

    # TODO: learn hashing algorithms
    def _hash(self, key):
        hashed_value = hash(key)
        dest_index = hashed_value % self.size
        return dest_index

    def __setitem__(self, key, value):
        dest_index = self._hash(key)
        curr_linked_list = self.buckets.array[dest_index]

        # if the bucket is empty, insert a new linked list
        if not curr_linked_list:
            new_linked_list = linked_list.LinkedList()
            new_linked_list.append((key, value))
            self.buckets.array[dest_index] = new_linked_list
        # else append to the existing linked list
        else:
            curr_linked_list.append((key, value))

    def __getitem__(self, key):
        dest_index = self._hash(key)
        curr_linked_list = self.buckets.array[dest_index]
        if not curr_linked_list:
            raise KeyError
        for tup in curr_linked_list:
            if tup[0] == key:
                return tup[1]
        raise KeyError

    # TODO: learn diff between __del__ and __delitem__ and del map[key] actual usage how to use ??
    def __del__(self):
        pass

    def __str__(self):
        """
        Returns a string representation of the HashMap for printing.
        """
        map_str = ""
        for i in range(len(self.buckets.array)):
            print("bucket index " + str(i) + ":", end="")
            if self.buckets.array[i]:
                for pair in self.buckets.array[i]:
                    print(pair, end=" ")
                print("\n")
            else:
                print(" Empty")
