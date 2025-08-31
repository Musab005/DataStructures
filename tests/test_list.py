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
        array1 = List(3)
        array1.insert(0, 1)
        array1.insert(0, 2)
        array1.insert(0, 3)
        assert array1 == [3, 2, 1]

    # insert at full capacity
    def test_insert_2(self):
        array1 = List(3)
        array1.insert(0, 1)
        array1.insert(1, 2)
        array1.insert(2, 3)
        array1.insert(2, 4)
        assert array1 == [1, 2, 4, 3]

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
        try:
            array1.remove(5)
        except ValueError as ve:
            assert ve

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

    def test_clear_1(self):
        array1 = List(3)
        array1.append(1)
        array1.append(1)
        array1.append(1)
        array1.clear()
        assert array1 == []

    def test_index_1(self):
        array1 = List(3)
        array1.append(1)
        array1.append(1)
        array1.append(2)
        assert array1.index(2) == 2
        assert array1.index(1, 0, 1) == 0

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

    # unsorted array with array length != array size
    def test_sort_3(self):
        list3 = List(10)
        list3.append(2)
        list3.append(3)
        list3.append(1)
        list3.append(0)
        list3.append(10)
        list3.sort()
        assert list3 == [0, 1, 2, 3, 10]

    # only one value exists
    def test_sort_4(self):
        list4 = List(3)
        list4.append(2)
        list4.sort()
        assert list4 == [2]

    # reverse sort and array length = array size
    def test_sort_5(self):
        list5 = List(3)
        list5.append(2)
        list5.append(1)
        list5.append(3)
        list5.sort(reverse=True)
        assert list5 == [3, 2, 1]

    # reverse sort and array length != array size
    def test_sort_6(self):
        list6 = List(10)
        list6.append(2)
        list6.append(1)
        list6.append(3)
        list6.append(5)
        list6.append(0)
        list6.append(0)
        list6.sort(reverse=True)
        assert list6 == [5, 3, 2, 1, 0, 0]

    # all equal values
    def test_sort_7(self):
        list7 = List(5)
        list7.append(1)
        list7.append(1)
        list7.append(1)
        list7.append(1)
        list7.append(1)
        list7.sort()
        assert list7 == [1, 1, 1, 1, 1]

    # sort at every iteration - worst case scenario
    def test_sort_8(self):
        list8 = List(5)
        list8.append(10)
        list8.append(9)
        list8.append(8)
        list8.append(7)
        list8.append(6)
        list8.sort()
        assert list8 == [6, 7, 8, 9, 10]

    # empty list
    def test_sort_9(self):
        list9 = List(5)
        list9.sort()
        assert list9 == []

    def exhaustive_test_1(self):
        array1 = List(5)
        array1.append(2)
        array1.insert(0, 4)
        array1.sort(reverse=True)
        assert array1.count(3) == 0
        array1.insert(3, 10)
        array1.append(5)
        array1.pop()
        array2 = array1.copy()
        assert array2 == [4, 2, None, 10]
        array2.sort()
        array2[2] = 5
        array2[3] = 5
        assert array2 == [2, 4, 5, 5]
