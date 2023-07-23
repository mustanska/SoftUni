import unittest

from Testing.List.extended_list import IntegerList


class IntegerListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 2, 3)

    def test_initialize_integer_list(self):
        self.assertEqual(3, len(self.integer_list.get_data()))
        self.assertEqual(3, len(self.integer_list._IntegerList__data))

    def test_integer_list_not_integer_elements(self):
        self.integer_list = IntegerList(1, 2, 6.5)

        self.assertEqual(2, len(self.integer_list.get_data()))
        self.assertEqual(2, len(self.integer_list._IntegerList__data))

    def test_integer_list_get_data(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_element_to_integer_list_raises(self):
        values_from_different_types = [4.5, "hello", [], {}, (), True]

        with self.assertRaises(ValueError) as ex:
            for value in values_from_different_types:
                self.integer_list.add(value)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_element_to_integer_list(self):
        self.assertEqual(3, len(self.integer_list.get_data()))

        self.integer_list.add(5)

        self.assertEqual(4, len(self.integer_list.get_data()))

    def test_remove_index_from_integer_list_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(4)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_from_integer_list(self):
        self.assertEqual(3, len(self.integer_list.get_data()))

        self.integer_list.remove_index(1)

        self.assertEqual(2, len(self.integer_list.get_data()))

    def test_get_from_integer_list_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(4)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_from_integer_list(self):
        self.assertEqual(2, self.integer_list.get(1))

    def test_insert_to_integer_list_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(5, 3)

        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(1, 6.5)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_to_integer_list(self):
        self.assertEqual(3, len(self.integer_list.get_data()))
        self.assertEqual(2, self.integer_list.get_data()[1])

        self.integer_list.insert(1, 5)

        self.assertEqual(4, len(self.integer_list.get_data()))
        self.assertEqual(5, self.integer_list.get_data()[1])

    def test_get_biggest_from_integer_list(self):
        self.assertEqual(3, self.integer_list.get_biggest())

    def test_get_index_from_integer_list(self):
        self.assertEqual(0, self.integer_list.get_index(1))


if __name__ == '__main__':
    unittest.main()
