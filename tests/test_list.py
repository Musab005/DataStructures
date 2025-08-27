from src.lists.list import List


class TestArrays:
    def test_insert_1(self):
        array1 = List(10)
        array1.append(1)
        assert array1.index(1) == 0

    def test_insert_2(self):
        array1 = List(3)
        array1.append(1)
        array1.append(2)
        array1.append(3)
        array1.append(4)
        assert array1.index(4) == 3

    def test_delete_1(self):
        array1 = List(3)
        array1.append(1)
        array1.append(2)
        array1.append(3)
        array1.delete(2)
        assert array1.index(2) == -1

    def test_delete_2(self):
        array1 = List(3)
        array1.append(1)
        array1.append(2)
        array1.append(3)
        array1.delete(3)
        assert array1.index(3) == -1
