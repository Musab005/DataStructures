from src.maps.map import Map


class TestMap:

    def test_empty_map(self):
        map1 = Map()
        assert str(map1) == ('index 0: Empty\n'
                             'index 1: Empty\n'
                             'index 2: Empty\n'
                             'index 3: Empty\n'
                             'index 4: Empty\n'
                             'index 5: Empty\n'
                             'index 6: Empty\n'
                             'index 7: Empty\n'
                             'index 8: Empty\n'
                             'index 9: Empty\n')

    def test_setitem(self):
        map1 = Map()
        map1['A'] = 9
        map1['B'] = 13
        map1['Z'] = 0
        map1['fdf'] = 987
        assert str(map1) == ('index 0: Empty\n'
                             'index 1: Empty\n'
                             'index 2: Empty\n'
                             'index 3: Empty\n'
                             'index 4: Empty\n'
                             'index 5: Empty\n'
                             'index 6: Empty\n'
                             'index 7: Empty\n'
                             'index 8: Empty\n'
                             'index 9: Empty\n')
