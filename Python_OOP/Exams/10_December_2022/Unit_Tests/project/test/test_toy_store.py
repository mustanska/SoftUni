from unittest import TestCase, main
from project.toy_store import ToyStore

class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()
    def test_initialize_toy_store(self):
        test_data = ["A", "B", "C", "D", "E", "F", "G"]
        for data in test_data:
            self.assertEqual(None, self.toy_store.toy_shelf[data])

    def test_add_toy(self):
        with self.assertRaises(Exception) as ex1:
            self.toy_store.add_toy("H", "toy_name")

        self.assertEqual("Shelf doesn't exist!", str(ex1.exception))

        self.assertEqual(None, self.toy_store.toy_shelf["A"])
        result = self.toy_store.add_toy("A", "toy_name")
        self.assertEqual("toy_name", self.toy_store.toy_shelf["A"])
        self.assertEqual("Toy:toy_name placed successfully!", result)

        with self.assertRaises(Exception) as ex2:
            self.toy_store.add_toy("A", "toy_name")

        self.assertEqual("toy_name", self.toy_store.toy_shelf["A"])
        self.assertEqual("Toy is already in shelf!", str(ex2.exception))

        with self.assertRaises(Exception) as ex3:
            self.toy_store.add_toy("A", "new_toy_name")

        self.assertEqual("toy_name", self.toy_store.toy_shelf["A"])
        self.assertEqual("Shelf is already taken!", str(ex3.exception))

    def test_remove_toy(self):
        self.toy_store.add_toy("A", "toy_name")

        with self.assertRaises(Exception) as ex1:
            self.toy_store.remove_toy("H", "toy_name")

        self.assertEqual("Shelf doesn't exist!", str(ex1.exception))

        with self.assertRaises(Exception) as ex2:
            self.toy_store.remove_toy("A", "other_toy_name")

        self.assertEqual("toy_name", self.toy_store.toy_shelf["A"])
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex2.exception))

        result = self.toy_store.remove_toy("A", "toy_name")
        self.assertEqual(None, self.toy_store.toy_shelf["A"])
        self.assertEqual("Remove toy:toy_name successfully!", result)


if __name__ == "__main__":
    main()