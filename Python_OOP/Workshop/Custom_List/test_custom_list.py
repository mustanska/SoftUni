from unittest import TestCase, main
from custom_list import CustomList

class TestCustomList(TestCase):
    def setUp(self) -> None:
        self.custom_list = CustomList(1, "hello", 3, [2, 3, 4], 5.5, 8, (1, "me"), 3, -2)

    def test_initialize_custom_list(self):
        excepted = [1, "hello", 3, [2, 3, 4], 5.5, 8, (1, "me"), 3, -2]
        self.assertEqual(excepted, self.custom_list.list)

    def test_custom_list_setter_with_empty_element_raises(self):
        with self.assertRaises(ValueError) as ve:
            test_list = CustomList(1, [])

        self.assertEqual("Element cannot be empty!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            test_list = CustomList(1, None)

        self.assertEqual("Element cannot be empty!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            test_list = CustomList(1, "")

        self.assertEqual("Element cannot be empty!", str(ve.exception))

    def test_custom_list_setter(self):
        test_list = CustomList(1, 0)
        self.assertEqual([1, 0], test_list.list)

    def test_index_validity_raises(self):
        with self.assertRaises(IndexError) as ie:
            self.custom_list._CustomList__check_index(20)

        self.assertEqual("Index is out of range!", str(ie.exception))

    def test_find_indices_by_not_existing_value_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.custom_list._CustomList__find_indices_by_value(2)

        self.assertEqual("The value does not exist in the list.", str(ve.exception))

    def test_find_indices_by_value(self):
        result = self.custom_list._CustomList__find_indices_by_value(3)
        self.assertEqual([2, 7], result)

    def test_check_non_iterable_object_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.custom_list._CustomList__check_iterable_object(1)

        self.assertEqual("This object is not iterable!", str(ve.exception))

    def test_is_empty_value(self):
        result = self.custom_list._CustomList__is_empty_value("")
        self.assertTrue(result)

        result = self.custom_list._CustomList__is_empty_value(None)
        self.assertTrue(result)

        result = self.custom_list._CustomList__is_empty_value(0)
        self.assertFalse(result)

        result = self.custom_list._CustomList__is_empty_value([1, 2, 3])
        self.assertFalse(result)

    def test_check_empty_element_to_add_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.custom_list._CustomList__check_element_to_add([])
        self.assertEqual("Element cannot be empty!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.custom_list._CustomList__check_element_to_add("")
        self.assertEqual("Element cannot be empty!", str(ve.exception))

    def test_get_values_of_elements_in_custom_list(self):
        result = self.custom_list._CustomList__get_values_of_elements()
        expected = [1, 5, 3, 3, 5.5, 8, 2, 3, -2]
        self.assertEqual(expected, result)

    def test_append_element_to_list(self):
        with self.assertRaises(ValueError) as ve:
            self.custom_list.append(None)
        self.assertEqual("Element cannot be empty!", str(ve.exception))

        result = self.custom_list.append(2)
        excepted = [1, "hello", 3, [2, 3, 4], 5.5, 8, (1, "me"), 3, -2, 2]
        self.assertEqual(excepted, result)

    def test_remove_element_from_list(self):
        with self.assertRaises(IndexError) as ie:
            self.custom_list.remove(10)
        self.assertEqual("Index is out of range!", str(ie.exception))

        result = self.custom_list.remove(5)
        excepted = [1, "hello", 3, [2, 3, 4], 5.5, (1, "me"), 3, -2]
        self.assertEqual(excepted, self.custom_list.list)
        self.assertEqual(8, result)

    def test_get_element_by_index(self):
        with self.assertRaises(IndexError) as ie:
            self.custom_list.get(10)
        self.assertEqual("Index is out of range!", str(ie.exception))

        result = self.custom_list.get(1)
        self.assertEqual("hello", result)

    def test_extend_list_with_non_iterable_element_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.custom_list.extend(1.5)

        self.assertEqual("This object is not iterable!", str(ve.exception))

        result = self.custom_list.extend(["hi", 11, "bye"])
        excepted = [1, "hello", 3, [2, 3, 4], 5.5, 8, (1, "me"), 3, -2, "hi", 11, "bye"]
        self.assertEqual(excepted, result)

    def test_insert_value_on_index(self):
        with self.assertRaises(IndexError) as ie:
            self.custom_list.insert(-10, ["hi", 11, "bye"])
        self.assertEqual("Index is out of range!", str(ie.exception))

        result = self.custom_list.insert(-5, ["hi", 11, "bye"])
        excepted = [1, "hello", 3, [2, 3, 4], ["hi", 11, "bye"], 5.5, 8, (1, "me"), 3, -2]
        self.assertEqual(excepted, result)

    def test_pop_last_element_from_list(self):
        result = self.custom_list.pop()
        self.assertEqual(-2, result)

    def test_clear_list(self):
        self.custom_list.clear()
        self.assertEqual([], self.custom_list.list)

    def test_index_of_value(self):
        with self.assertRaises(ValueError) as ve:
            self.custom_list.index(0)

        self.assertEqual("The value does not exist in the list.", str(ve.exception))

        result = self.custom_list.index(5.5)
        self.assertEqual(4, result)

    def test_count_of_value(self):
        result = self.custom_list.count([1, 2])
        self.assertEqual(0, result)

        result = self.custom_list.count(3)
        self.assertEqual(2, result)

    def test_reverse_list_method(self):
        result = self.custom_list.reverse()
        expected = [-2, 3, (1, "me"), 8, 5.5, [2, 3, 4], 3, "hello", 1]
        self.assertEqual(expected, result)

    def test_copy_list_method(self):
        result = self.custom_list.copy()
        expected = [1, "hello", 3, [2, 3, 4], 5.5, 8, (1, "me"), 3, -2]
        self.assertEqual(expected, result)
        self.assertNotEqual(id(result), id(self.custom_list.list))

    def test_size_list_method(self):
        result = self.custom_list.size()
        self.assertEqual(9, result)

    def test_add_first_element_in_list(self):
        self.custom_list.add_first(0)
        expected = [0, 1, "hello", 3, [2, 3, 4], 5.5, 8, (1, "me"), 3, -2]
        self.assertEqual(expected, self.custom_list.list)
        self.assertEqual(0, self.custom_list.list[0])

    

if __name__ == "__main__":
    main()
