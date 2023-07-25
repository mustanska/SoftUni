from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train("Speed Train", 50)

    def test_default_class_attributes_from_train(self):
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_initialize_instance_from_train_class(self):
        self.assertEqual("Speed Train", self.train.name)
        self.assertEqual(50, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passenger_to_train_if_train_is_full_raises(self):
        self.train.capacity = 2
        self.train.passengers = ["Passenger1", "Passenger2"]

        with self.assertRaises(ValueError) as ve:
            self.train.add("Passenger3")

        self.assertEqual(self.train.TRAIN_FULL, str(ve.exception))

    def test_add_passenger_to_train_if_passenger_already_exist_raises(self):
        self.train.passengers = ["Passenger"]

        with self.assertRaises(ValueError) as ve:
            self.train.add("Passenger")

        self.assertEqual(self.train.PASSENGER_EXISTS.format("Passenger"), str(ve.exception))

    def test_add_passenger_to_train_allowed(self):
        result = self.train.add("Passenger")
        self.assertEqual(["Passenger"], self.train.passengers)
        self.assertEqual(self.train.PASSENGER_ADD.format("Passenger"), result)

    def test_remove_passenger_from_train_if_not_exist_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Passenger")

        self.assertEqual(self.train.PASSENGER_NOT_FOUND.format("Passenger"), str(ve.exception))

    def test_remove_passenger_from_train_allowed(self):
        self.train.passengers = ["Passenger"]
        result = self.train.remove("Passenger")
        self.assertEqual([], self.train.passengers)
        self.assertEqual(self.train.PASSENGER_REMOVED.format("Passenger"), result)

if __name__ == "__main__":
    main()