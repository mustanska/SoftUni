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

    



if __name__ == "__main__":
    main()