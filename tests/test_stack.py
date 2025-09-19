from src.stacks.stack import Stack
import pytest


class TestStack:

    def test_push_1(self):
        stack1 = Stack()
        stack1.push(1)
        stack1.push(10)
        stack1.push(5)
        assert str(stack1) == "5 -> 10 -> 1 -> None"

    def test_pop_1(self):
        stack1 = Stack()
        stack1.push(1)
        stack1.push(10)
        stack1.push(5)
        stack1.pop()
        stack1.pop()
        assert str(stack1) == "1 -> None"

    def test_peek_1(self):
        stack1 = Stack()
        stack1.push(1)
        stack1.push(10)
        stack1.push(5)
        assert stack1.peek() == 5

    def test_isempty_1(self):
        stack1 = Stack()
        stack1.push(1)
        stack1.push(10)
        stack1.push(5)
        assert not stack1.is_empty()

    def test_isempty_2(self):
        stack2 = Stack()
        stack2.push(1)
        stack2.push(10)
        stack2.push(5)
        stack2.pop()
        stack2.pop()
        stack2.pop()
        assert stack2.is_empty()

    def test_isempty_3(self):
        stack3 = Stack()
        assert stack3.is_empty()

    def test_len_1(self):
        stack1 = Stack()
        assert len(stack1) == 0

    def test_len_2(self):
        stack2 = Stack()
        stack2.push(1)
        stack2.push(2)
        stack2.push(3)
        assert len(stack2) == 3

    def test_len_3(self):
        stack2 = Stack()
        stack2.push(1)
        stack2.push(2)
        stack2.pop()
        assert len(stack2) == 1

    # A fixture to provide an empty list for tests
    @pytest.fixture
    def empty_list(self):
        return Stack()

    # A fixture to provide a list with one item
    @pytest.fixture
    def single_item_list(self):
        ll = Stack()
        ll.push(10)
        return ll

    # A fixture to provide a list with multiple items
    @pytest.fixture
    def populated_list(self):
        ll = Stack()
        ll.push("A")
        ll.push("B")
        ll.push("C")
        return ll

    def test_for_loop_and_list_conversion(self, populated_list):
        """
        Tests if the linked list can be iterated over with a for loop
        and if it can be correctly converted to a Python list.
        """
        # Create a known-correct list to compare against
        python_list = ["C", "B", "A"]

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
        expected_full_list = ["C", "B", "A"]

        # The outer loop uses its own iterator ("walker")
        for outer_item in populated_list:
            # The inner loop should get a NEW, fresh iterator ("walker") every time
            inner_items = []
            for inner_item in populated_list:
                inner_items.append(inner_item)

            # We assert that the inner loop ALWAYS produces the full, correct list,
            # regardless of where the outer loop's iterator is.
            assert inner_items == expected_full_list
