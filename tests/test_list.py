import pytest

from src.lists.list import List


class TestArrays:

    # append at full-capacity
    def test_append_1(self):
        array1 = List(3)
        array1.append(1)
        array1.append(2)
        array1.append(3)
        array1.append(4)
        assert array1 == [1, 2, 3, 4]

    # append within capacity
    def test_append_2(self):
        array1 = List(3)
        array1.append(1)
        array1.append(2)
        assert array1 == [1, 2]

    # insert within capacity
    def test_insert_1(self):
        list1 = List(3)
        list1.insert(0, 1)
        list1.insert(0, 2)
        list1.insert(0, 3)
        assert list1 == [3, 2, 1]

    # insert at full capacity
    def test_insert_2(self):
        list2 = List(3)
        list2.insert(0, 1)
        list2.insert(1, 2)
        list2.insert(2, 3)
        list2.insert(2, 4)
        assert list2 == [1, 2, 4, 3]

    # insert outside size
    def test_insert_3(self):
        list2 = List(3)
        list2.insert(0, 1)
        list2.insert(1, 2)
        list2.insert(2, 3)
        list2.insert(3, 5)
        assert list2 == [1, 2, 3, 5]

    # insert after a gap but within size
    def test_insert_4(self):
        list4 = List(5)
        list4.insert(0, 1)
        list4.insert(3, 3)
        assert list4 == [1, 3]

    # remove from end
    def test_remove_1(self):
        array1 = List(3)
        array1.append(1)
        array1.append(2)
        array1.append(3)
        array1.remove(3)
        assert array1 == [1, 2]

    # remove from middle
    def test_remove_2(self):
        array1 = List(3)
        array1.append(1)
        array1.append(2)
        array1.append(3)
        array1.remove(2)
        assert array1 == [1, 3]

    # remove non-existing value
    def test_remove_3(self):
        array1 = List(3)
        array1.append(1)
        array1.append(2)
        array1.append(3)
        with pytest.raises(ValueError):
            array1.remove(5)

    # remove first occurrence only
    def test_remove_4(self):
        array1 = List(3)
        array1.append(1)
        array1.append(1)
        array1.remove(1)
        assert array1 == [1]

    # default pop
    def test_pop_1(self):
        array1 = List(3)
        array1.append(1)
        array1.append(1)
        array1.pop()
        assert array1 == [1]

    # pop from beginning
    def test_pop_2(self):
        array1 = List(3)
        array1.append(1)
        array1.append(1)
        array1.pop(0)
        assert array1 == [1]

    # clear array
    def test_clear_1(self):
        array1 = List(3)
        array1.append(1)
        array1.append(1)
        array1.append(1)
        array1.clear()
        assert array1 == []

    # normal index operation
    def test_index_1(self):
        array1 = List(3)
        array1.append(1)
        array1.append(1)
        array1.append(2)
        assert array1.index(2) == 2

    # Non-existing index operation
    def test_index_2(self):
        array1 = List(3)
        array1.append(1)
        array1.append(1)
        array1.append(2)
        with pytest.raises(ValueError):
            array1.index(3)

    # Valid index but None value
    def test_index_3(self):
        array1 = List(5)
        array1.append(1)
        array1.append(1)
        array1.append(2)
        try:
            array1.index(3)
        except ValueError as ve:
            assert ve

    # valid subsequence and value exists
    def test_index_4(self):
        array1 = List(3)
        array1.append(1)
        array1.append(1)
        array1.append(2)
        assert array1.index(1, 0, 1) == 0

    # invalid subsequence
    def test_index_5(self):
        array1 = List(3)
        array1.append(1)
        array1.append(1)
        array1.append(2)
        with pytest.raises(ValueError):
            array1.index(1, 0, 10)

    # valid subsequence but value does not exist
    def test_index_6(self):
        array1 = List(10)
        array1.append(1)
        array1.append(1)
        array1.append(2)
        array1.append(3)
        array1.append(3)
        with pytest.raises(ValueError):
            array1.index(1, 2, 5)

    # valid subsequence but over None values
    def test_index_7(self):
        array1 = List(10)
        array1.append(1)
        array1.append(1)
        array1.append(2)
        array1.append(3)
        array1.append(3)
        with pytest.raises(ValueError):
            array1.index(1, 7, 9)

    def test_count_1(self):
        array1 = List(3)
        array1.append(1)
        array1.append(1)
        array1.append(2)
        assert array1.count(1) == 2

    def test_reverse_1(self):
        array1 = List(3)
        array1.append(1)
        array1.append(2)
        array1.append(3)
        array1.reverse()
        assert array1 == [3, 2, 1]

    def test_copy_1(self):
        array1 = List(3)
        array1.append(1)
        array1.append(2)
        array2 = array1.copy()
        assert array1 == array2

    # already sorted array and array length = array size
    def test_sort_1(self):
        list1 = List(3)
        list1.append(1)
        list1.append(2)
        list1.append(3)
        list1.sort()
        assert list1 == [1, 2, 3]

    # already sorted array and array length != array size
    def test_sort_1_1(self):
        list1_1 = List(5)
        list1_1.append(1)
        list1_1.append(2)
        list1_1.append(3)
        list1_1.sort()
        assert list1_1 == [1, 2, 3]

    # unsorted array and array length = array size
    def test_sort_2(self):
        list2 = List(5)
        list2.append(2)
        list2.append(3)
        list2.append(1)
        list2.append(7)
        list2.append(0)
        list2.sort()
        assert list2 == [0, 1, 2, 3, 7]

    # unsorted array and array length != array size
    def test_sort_2_1(self):
        list2_1 = List(10)
        list2_1.append(2)
        list2_1.append(3)
        list2_1.append(1)
        list2_1.append(0)
        list2_1.append(10)
        list2_1.sort()
        assert list2_1 == [0, 1, 2, 3, 10]

    # only one value exists
    def test_sort_3(self):
        list3 = List(3)
        list3.append(2)
        list3.sort()
        assert list3 == [2]

    # empty list
    def test_sort_4(self):
        list4 = List(3)
        list4.sort()
        assert list4 == []

    # reverse sort and array length = array size
    def test_sort_5_1(self):
        list5_1 = List(3)
        list5_1.append(2)
        list5_1.append(1)
        list5_1.append(3)
        list5_1.sort(reverse=True)
        assert list5_1 == [3, 2, 1]

    # reverse sort and array length != array size
    def test_sort_5_2(self):
        list5_2 = List(10)
        list5_2.append(2)
        list5_2.append(1)
        list5_2.append(3)
        list5_2.append(5)
        list5_2.append(0)
        list5_2.append(0)
        list5_2.sort(reverse=True)
        assert list5_2 == [5, 3, 2, 1, 0, 0]

    # reverse sort and array already reverse sorted
    def test_sort_5_3(self):
        list5_3 = List(10)
        list5_3.append(9)
        list5_3.append(8)
        list5_3.append(7)
        list5_3.append(6)
        list5_3.append(5)
        list5_3.append(4)
        list5_3.sort(reverse=True)
        assert list5_3 == [9, 8, 7, 6, 5, 4]

    # all equal values and array length = array size
    def test_sort_6(self):
        list6 = List(5)
        list6.append(1)
        list6.append(1)
        list6.append(1)
        list6.append(1)
        list6.append(1)
        list6.sort()
        assert list6 == [1, 1, 1, 1, 1]

    # all equal values and array length != array size
    def test_sort_6_1(self):
        list6_1 = List(10)
        list6_1.append(2)
        list6_1.append(2)
        list6_1.append(2)
        list6_1.append(2)
        list6_1.append(2)
        list6_1.sort()
        assert list6_1 == [2, 2, 2, 2, 2]

    # sort at every iteration - worst case scenario and array length = array size
    def test_sort_7_1(self):
        list7_1 = List(5)
        list7_1.append(10)
        list7_1.append(9)
        list7_1.append(8)
        list7_1.append(7)
        list7_1.append(6)
        list7_1.sort()
        assert list7_1 == [6, 7, 8, 9, 10]

    # sort at every iteration - worst case scenario and array length != array size
    def test_sort_7_2(self):
        list7_2 = List(10)
        list7_2.append(9)
        list7_2.append(8)
        list7_2.append(7)
        list7_2.append(6)
        list7_2.append(5)
        list7_2.sort()
        assert list7_2 == [5, 6, 7, 8, 9]

    # sort at every iteration (reverse) - worst case scenario and array length = array size
    def test_sort_8_1(self):
        list7_1 = List(5)
        list7_1.append(1)
        list7_1.append(2)
        list7_1.append(3)
        list7_1.append(4)
        list7_1.append(5)
        list7_1.sort(reverse=True)
        assert list7_1 == [5, 4, 3, 2, 1]

    # sort at every iteration (reverse) - worst case scenario and array length != array size
    def test_sort_8_2(self):
        list7_2 = List(10)
        list7_2.append(5)
        list7_2.append(6)
        list7_2.append(7)
        list7_2.append(8)
        list7_2.append(9)
        list7_2.sort(reverse=True)
        assert list7_2 == [9, 8, 7, 6, 5]

    # empty list
    def test_sort_9(self):
        list9 = List(5)
        list9.sort()
        assert list9 == []
