from src.linkedlists.linked_list import LinkedList
class Test_linked_list:

    # simple append operations
    def test_append_1(self):
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        list1.append(3)
        assert str(list1) == "1 -> 2 -> 3 -> None"

    # simple prepend operations
    def test_prepend_1(self):
        list1 = LinkedList()
        list1.prepend(1)
        list1.prepend(2)
        list1.prepend(3)
        assert str(list1) == "3 -> 2 -> 1 -> None"

    # combination of append/prepend operations
    def test_append_prepend_1(self):
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        list1.prepend(3)
        list1.append(5)
        list1.prepend(9)
        list1.prepend(10)
        list1.append(7)
        assert str(list1) == "10 -> 9 -> 3 -> 1 -> 2 -> 5 -> 7 -> None"

    def test_reverse_1(self):
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        list1.append(3)
        list1.reverse()
        assert str(list1) == "3 -> 2 -> 1 -> None"

    def test_reverse_2(self):
        list2 = LinkedList()
        list2.append(1)
        list2.append(2)
        list2.append(3)
        list2.reverse_2()
        assert str(list2) == "3 -> 2 -> 1 -> None"

    def test_middle_1(self):
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        list1.append(3)
        list1.append(4)
        assert list1.find_middle() == 2

    def test_middle_2(self):
        list2 = LinkedList()
        list2.append(1)
        list2.append(2)
        list2.append(3)
        list2.append(4)
        list2.append(5)
        assert list2.find_middle() == 3

    def get_at_1(self):
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        list1.append(3)
        list1.append(4)
        assert list1.get_at(2) == 3

    # TODO: check if this is the right way to test an exception
    def get_at_2(self):
        list2 = LinkedList()
        list2.append(1)
        list2.append(2)
        list2.append(3)
        list2.append(4)
        try:
            list2.get_at(199)
        except IndexError as e:
            raise e
