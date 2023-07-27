from unittest import TestCase, main
from project.plantation import Plantation

class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(50)

    def test_initialize_plantation_instance(self):
        self.assertEqual(50, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_set_size_of_plantation_less_than_zero_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_set_size_of_plantation(self):
        self.plantation.size = 0
        self.assertEqual(0, self.plantation.size)

    def test_hire_existing_worker_raises(self):
        self.plantation.workers = ["Ivan"]

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Ivan")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_allowed(self):
        result = self.plantation.hire_worker("Ivan")
        self.assertEqual(["Ivan"], self.plantation.workers)
        self.assertEqual("Ivan successfully hired.", result)

    def test_overwritten_method_len_for_count_of_plantation(self):
        self.assertEqual(0, len(self.plantation))
        self.plantation.plants["Ivan"] = ["rose", "orchid"]
        self.assertEqual({"Ivan": ["rose", "orchid"]}, self.plantation.plants)
        self.assertEqual(2, len(self.plantation))

    def test_overwritten_method_len_for_count_of_plantation_with_two_workers(self):
        self.assertEqual(0, len(self.plantation))
        self.plantation.plants["Ivan"] = ["rose", "orchid"]
        self.plantation.plants["Maria"] = ["lemon"]
        self.assertEqual({"Ivan": ["rose", "orchid"], "Maria": ["lemon"]}, self.plantation.plants)
        self.assertEqual(3, len(self.plantation))

    def test_planting_in_plantation_without_existing_worker_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivan", "rose")

        self.assertEqual("Worker with name Ivan is not hired!", str(ve.exception))

    def test_planting_in_plantation_with_no_empty_spaces_raises(self):
        self.plantation.workers = ["Ivan"]
        self.plantation.plants = {"Ivan": ["orchid"]}
        self.plantation.size = 1

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivan", "rose")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_in_plantation_if_worker_in_plants(self):
        self.plantation.workers = ["Ivan"]
        self.plantation.plants["Ivan"] = ["orchid"]
        result = self.plantation.planting("Ivan", "rose")
        self.assertEqual("Ivan planted rose.", result)
        self.assertEqual({"Ivan": ["orchid", "rose"]}, self.plantation.plants)

    def test_planting_in_plantation_if_worker_not_in_plants(self):
        self.plantation.workers = ["Ivan"]
        result = self.plantation.planting("Ivan", "rose")
        self.assertEqual("Ivan planted it's first rose.", result)
        self.assertEqual({"Ivan": ["rose"]}, self.plantation.plants)

    def test_overwritten_method_str_for_plantation_without_workers_and_plants(self):
        self.assertEqual("Plantation size: 50\n", str(self.plantation))

    def test_overwritten_method_str_for_plantation_with_workers_and_without_plants(self):
        self.plantation.workers = ["Ivan", "Petyr"]
        expected = "Plantation size: 50\nIvan, Petyr"
        self.assertEqual(expected, str(self.plantation))

    def test_overwritten_method_str_for_plantation_without_workers_and_with_plants(self):
        self.plantation.plants = {"Ivan": ["rose", "orchid"], "Petyr": ["lemon", "orange"]}
        expected = "Plantation size: 50\n\nIvan planted: rose, orchid\nPetyr planted: lemon, orange"
        self.assertEqual(expected, str(self.plantation))

    def test_overwritten_method_str_for_plantation_with_workers_and_plants(self):
        self.plantation.workers = ["Ivan", "Petyr"]
        self.plantation.plants = {"Ivan": ["rose", "orchid"], "Petyr": ["lemon", "orange"]}
        expected = "Plantation size: 50\nIvan, Petyr\nIvan planted: rose, orchid\nPetyr planted: lemon, orange"
        self.assertEqual(expected, str(self.plantation))

    def test_represent_plantation_without_workers(self):
        self.assertEqual("Size: 50\nWorkers: ", self.plantation.__repr__())

    def test_represent_plantation_with_workers(self):
        self.plantation.workers = ["Ivan", "Petyr"]
        self.assertEqual("Size: 50\nWorkers: Ivan, Petyr", self.plantation.__repr__())

if __name__ == "__main__":
    main()