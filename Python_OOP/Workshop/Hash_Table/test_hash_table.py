from unittest import TestCase, main
from hash_table import HashTable

class TestHashTable(TestCase):
    def setUp(self) -> None:
        self.hash_table = HashTable()

    def test_initialize_hash_table(self):
        self.assertEqual(4, self.hash_table.MAX_SIZE)
        self.assertEqual(4, self.hash_table._HashTable__max_capacity)
        self.assertEqual(0, self.hash_table._HashTable__length)
        self.assertEqual([None, None, None, None], self.hash_table._HashTable__keys)
        self.assertEqual([None, None, None, None], self.hash_table._HashTable__values)

    def test_check_key_is_not_string_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.hash_table._HashTable__check_key(123)

        self.assertEqual("The key is not a string!", str(ve.exception))

    def test_calculate_index_by_key(self):
        result = self.hash_table._HashTable__calculate_index("Key")
        self.assertEqual(1, result)

    def test_check_index(self):
        result = self.hash_table._HashTable__check_index(1)
        self.assertEqual(1, result)

    def test_increase_capacity(self):
        self.hash_table._HashTable__increase_capacity()
        self.assertEqual([None, None, None, None, None, None, None, None], self.hash_table._HashTable__keys)
        self.assertEqual([None, None, None, None, None, None, None, None], self.hash_table._HashTable__values)
        self.assertEqual(8, self.hash_table._HashTable__max_capacity)

    def test_hash(self):
        result = self.hash_table.hash("Key")
        self.assertEqual(1, result)

    def test_add(self):
        self.hash_table.add("Key", 1)
        self.assertEqual([None, "Key", None, None], self.hash_table._HashTable__keys)
        self.assertEqual([None, 1, None, None], self.hash_table._HashTable__values)
        self.assertEqual("{Key: 1}", str(self.hash_table))

        self.hash_table.add("SomeKey", 2)
        self.assertEqual([None, "Key", "SomeKey", None], self.hash_table._HashTable__keys)
        self.assertEqual([None, 1, 2, None], self.hash_table._HashTable__values)
        self.assertEqual("{Key: 1, SomeKey: 2}", str(self.hash_table))

        self.hash_table.add("OtherKey", 3)
        self.assertEqual([None, "Key", "SomeKey", "OtherKey"], self.hash_table._HashTable__keys)
        self.assertEqual([None, 1, 2, 3], self.hash_table._HashTable__values)
        self.assertEqual("{Key: 1, SomeKey: 2, OtherKey: 3}", str(self.hash_table))

        self.hash_table.add("NewKey", 4)
        self.assertEqual(["NewKey", "Key", "SomeKey", "OtherKey"], self.hash_table._HashTable__keys)
        self.assertEqual([4, 1, 2, 3], self.hash_table._HashTable__values)
        self.assertEqual("{NewKey: 4, Key: 1, SomeKey: 2, OtherKey: 3}", str(self.hash_table))

        self.hash_table.add("LastKey", 5)
        self.assertEqual(["NewKey", "Key", "SomeKey", "OtherKey", "LastKey", None, None, None], self.hash_table._HashTable__keys)
        self.assertEqual([4, 1, 2, 3, 5, None, None, None], self.hash_table._HashTable__values)
        self.assertEqual("{NewKey: 4, Key: 1, SomeKey: 2, OtherKey: 3, LastKey: 5}", str(self.hash_table))

    def test_get(self):
        result = self.hash_table.get("Key")
        self.assertEqual(None, result)

        result = self.hash_table.get("NewKey", "The key does not exist!")
        self.assertEqual("The key does not exist!", result)

        self.hash_table.add("Key", 1)
        result = self.hash_table.get("Key")
        self.assertEqual(1, result)

    def test_keys(self):
        result = self.hash_table.keys()
        self.assertEqual([], result)

        self.hash_table.add("Key", 1)
        self.hash_table.add("NewKey", [1, 2, 3])
        result = self.hash_table.keys()
        self.assertEqual(["Key", "NewKey"], result)

    def test_values(self):
        result = self.hash_table.values()
        self.assertEqual([], result)

        self.hash_table.add("Key", 1)
        self.hash_table.add("NewKey", [1, 2, 3])
        result = self.hash_table.values()
        self.assertEqual([1, [1, 2, 3]], result)

    def test_items(self):
        result = self.hash_table.items()
        self.assertEqual([], result)

        self.hash_table.add("Key", 1)
        self.hash_table.add("NewKey", [1, 2, 3])
        result = self.hash_table.items()
        self.assertEqual([("Key", 1), ("NewKey", [1, 2, 3])], result)

if __name__ == "__main__":
    main()