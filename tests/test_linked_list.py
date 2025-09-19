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

    # A fixture to provide an empty list for tests
    @pytest.fixture
    def empty_list(self):
        return LinkedList()

    # A fixture to provide a list with one item
    @pytest.fixture
    def single_item_list(self):
        ll = LinkedList()
        ll.append(10)
        return ll

    # A fixture to provide a list with multiple items
    @pytest.fixture
    def populated_list(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("C")
        return ll

    def test_for_loop_and_list_conversion(self, populated_list):
        """
        Tests if the linked list can be iterated over with a for loop
        and if it can be correctly converted to a Python list.
        """
        # Create a known-correct list to compare against
        python_list = ["A", "B", "C"]

        # 1. Test by direct conversion to a list
        # This is a concise and powerful test of the full iterator protocol
        assert list(populated_list) == python_list

        # 2. Test explicitly with a for loop
        iterated_items = []
        for item in populated_list:
            iterated_items.append(item)

        assert iterated_items == python_list

    def test_iteration_on_empty_list(self, empty_list):
        """
        Tests that iterating over an empty list produces no items and exits cleanly.
        """
        for _ in empty_list:
            # If this loop ever runs, something is wrong.
            pytest.fail("Iterator for an empty list should not yield any items.")
        # If the loop finishes without failing, the test passes.
        assert True

    def test_iteration_on_single_item_list(self, single_item_list):
        """
        Tests iteration on a list with exactly one item.
        """
        assert list(single_item_list) == [10]

    def test_iterator_independence(self, populated_list):
        """
        Tests that two iterators created from the same list are independent.
        This is the most important test for the iterator pattern.
        """
        expected_full_list = ["A", "B", "C"]

        # The outer loop uses its own iterator ("walker")
        for outer_item in populated_list:
            # The inner loop should get a NEW, fresh iterator ("walker") every time
            inner_items = []
            for inner_item in populated_list:
                inner_items.append(inner_item)

            # We assert that the inner loop ALWAYS produces the full, correct list,
            # regardless of where the outer loop's iterator is.
            assert inner_items == expected_full_list
