import pytest
from src.maps.map import Map


class TestMap:

    def test_init(self):
        """Test that the map is initialized correctly."""
        m = Map(size=16)
        assert m.size == 16
        assert len(m) == 0
        assert m.count == 0

    def test_set_and_get_item(self):
        """Test basic setting and getting of items."""
        m = Map()
        m['name'] = 'Kevin'
        m['age'] = 30
        assert m['name'] == 'Kevin'
        assert m['age'] == 30
        assert len(m) == 2

    def test_update_item(self):
        """Test that setting an existing key updates the value."""
        m = Map()
        m['city'] = 'New York'
        assert m['city'] == 'New York'
        assert len(m) == 1

        m['city'] = 'San Francisco'
        assert m['city'] == 'San Francisco'
        assert len(m) == 1  # VERY IMPORTANT: count should not increase

    def test_key_error_on_get(self):
        """Test that getting a non-existent key raises KeyError."""
        m = Map()
        with pytest.raises(KeyError):
            value = m['non_existent_key']

    def test_contains(self):
        """Test the 'in' operator."""
        m = Map()
        m['a'] = 1
        assert m.count == 1
        assert 'a' in m
        assert 'b' not in m

    def test_del_item(self):
        """Test deleting an item."""
        m = Map()
        m['a'] = 1
        m['b'] = 2
        assert len(m) == 2

        del m['a']
        assert len(m) == 1
        assert 'a' not in m
        assert m['b'] == 2

    def test_key_error_on_del(self):
        """Test that deleting a non-existent key raises KeyError."""
        m = Map()
        m['a'] = 1
        with pytest.raises(KeyError):
            del m['non_existent_key']

    def test_collision(self):
        """
        Test that the map correctly handles hash collisions.
        This requires knowing two keys that will hash to the same index.
        We can "mock" the hash function or just find two by trial and error.
        Let's assume 'key1' and 'key11' collide in a map of size 10.
        hash('key1') % 10 will be the same as hash('key11') % 10.
        """
        m = Map(size=10)

        # These keys need to have the same hash value modulo 10
        # This is a bit of a trick to force a collision for testing
        class MockKey:
            def __init__(self, value, hash_val):
                self.value = value
                self._hash_val = hash_val

            def __hash__(self):
                return self._hash_val

            def __eq__(self, other):
                return self.value == other.value

        key1 = MockKey('key1', 15)  # -> hashes to index 5
        key2 = MockKey('key2', 25)  # -> also hashes to index 5

        m[key1] = 'value1'
        m[key2] = 'value2'

        assert len(m) == 2
        assert m[key1] == 'value1'
        assert m[key2] == 'value2'

        # Now let's check that the internal structure is a linked list at index 5
        # This is a "white-box" test, which is okay for data structures
        bucket_index = m._hash(key1)
        assert bucket_index == 5
        assert m.buckets.array[bucket_index] is not None
        assert len(m.buckets.array[bucket_index]) == 2
