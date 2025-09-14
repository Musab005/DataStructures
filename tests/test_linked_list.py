import pytest

from src.linkedlists.linked_list import LinkedList


class TestLinkedList:

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

    def test_get_at_1(self):
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        list1.append(3)
        list1.append(4)
        assert list1.get_at(2) == 3

    def test_get_at_2(self):
        list2 = LinkedList()
        list2.append(1)
        list2.append(2)
        list2.append(3)
        list2.append(4)
        with pytest.raises(IndexError):
            list2.get_at(199)

    # insert at middle
    def test_insert_at_1(self):
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        list1.append(3)
        list1.append(4)
        list1.insert_at(2, 3)
        assert str(list1) == "1 -> 2 -> 3 -> 3 -> 4 -> None"

    # insert at beginning
    def test_insert_at_2(self):
        list2 = LinkedList()
        list2.append(1)
        list2.append(2)
        list2.append(3)
        list2.append(4)
        list2.insert_at(0, 3)
        assert str(list2) == "3 -> 1 -> 2 -> 3 -> 4 -> None"

    # insert at end/out-of-bounds
    def test_insert_at_3(self):
        list3 = LinkedList()
        list3.append(1)
        list3.append(2)
        list3.append(3)
        list3.append(4)
        list3.insert_at(10, 5)
        assert str(list3) == "1 -> 2 -> 3 -> 4 -> 5 -> None"

    # remove first from empty list
    def test_remove_first_1(self):
        list1 = LinkedList()
        list1.remove_first()
        assert str(list1) == "None"

    # remove first normally
    def test_remove_first_2(self):
        list2 = LinkedList()
        list2.append(1)
        list2.append(2)
        list2.append(3)
        list2.remove_first()
        assert str(list2) == "2 -> 3 -> None"

    # remove last from empty list
    def test_remove_last_1(self):
        list1 = LinkedList()
        list1.remove_last()
        assert str(list1) == "None"

    # remove last normally
    def test_remove_last_2(self):
        list2 = LinkedList()
        list2.append(1)
        list2.append(2)
        list2.append(3)
        list2.remove_last()
        assert str(list2) == "1 -> 2 -> None"

    # remove last from list with one node
    def test_remove_last_3(self):
        list3 = LinkedList()
        list3.append(1)
        list3.remove_last()
        assert str(list3) == "None"

    # remove middle value
    def test_remove_by_value_1(self):
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        list1.append(3)
        list1.remove_by_value(2)
        assert str(list1) == "1 -> 3 -> None"

    # remove non-existing value
    def test_remove_by_value_2(self):
        list2 = LinkedList()
        list2.append(1)
        list2.append(2)
        list2.append(3)
        list2.remove_by_value(9)
        assert str(list2) == "1 -> 2 -> 3 -> None"

    # remove last value
    def test_remove_by_value_3(self):
        list3 = LinkedList()
        list3.append(1)
        list3.append(2)
        list3.append(3)
        list3.remove_by_value(3)
        assert str(list3) == "1 -> 2 -> None"

    # remove first value
    def test_remove_by_value_4(self):
        list4 = LinkedList()
        list4.append(1)
        list4.append(2)
        list4.append(3)
        list4.remove_by_value(1)
        assert str(list4) == "2 -> 3 -> None"

    # search non-existing value
    def test_search_1(self):
        list1 = LinkedList()
        list1.append(1)
        list1.append(2)
        list1.append(3)
        assert list1.search(10) is None

    # search existing value
    def test_search_2(self):
        list2 = LinkedList()
        list2.append(1)
        list2.append(2)
        list2.append(3)
        assert list2.search(2) == LinkedList.Node(2)

