from unittest import TestCase, main
from project.second_hand_car import SecondHandCar

class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.secondhand_car = SecondHandCar("Mercedes", "Cabriolet", 200, 1000)

    def test_initialize_secondhand_car(self):
        self.assertEqual("Mercedes", self.secondhand_car.model)
        self.assertEqual("Cabriolet", self.secondhand_car.car_type)
        self.assertEqual(200, self.secondhand_car.mileage)
        self.assertEqual(1000, self.secondhand_car.price)
        self.assertEqual([], self.secondhand_car.repairs)

    def test_price_less_than_or_equal_to_one_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.secondhand_car.price = 1

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.secondhand_car.price = 0.9

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_price_setter(self):
        self.secondhand_car.price = 1.1
        self.assertEqual(1.1, self.secondhand_car.price)

    def test_mileage_less_than_or_equal_to_hundred_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.secondhand_car.mileage = 100

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.secondhand_car.mileage = 99

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_mileage_setter(self):
        self.secondhand_car.mileage = 101
        self.assertEqual(101, self.secondhand_car.mileage)

    def test_set_promotional_price_greater_than_or_equal_to_current_price_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.secondhand_car.set_promotional_price(1000)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.secondhand_car.set_promotional_price(1001)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_set_promotional_price_successfully(self):
        result = self.secondhand_car.set_promotional_price(900)
        self.assertEqual(900, self.secondhand_car.price)
        self.assertEqual("The promotional price has been successfully set.", result)

    def test_need_repair(self):
        result = self.secondhand_car.need_repair(501, "Engine change")
        self.assertEqual(1000, self.secondhand_car.price)
        self.assertEqual("Repair is impossible!", result)

        result = self.secondhand_car.need_repair(499, "Engine change")
        self.assertEqual(1499, self.secondhand_car.price)
        self.assertEqual(["Engine change"], self.secondhand_car.repairs)
        self.assertEqual("Price has been increased due to repair charges.", result)

    def test_car_greater_than_another_car_with_different_type(self):
        other = SecondHandCar("BMW", "Sedan", 150, 500)
        self.assertEqual("Cars cannot be compared. Type mismatch!", self.secondhand_car > other)

    def test_car_greater_than_another_car_with_same_type(self):
        other = SecondHandCar("BMW", "Cabriolet", 150, 500)
        self.assertEqual(True, self.secondhand_car > other)

        other.price = 1000
        self.assertEqual(False, self.secondhand_car > other)

        other.price = 1500
        self.assertEqual(False, self.secondhand_car > other)

    def test_string_representation_of_secondhand_car(self):
        expected ="""Model Mercedes | Type Cabriolet | Milage 200km\nCurrent price: 1000.00 | Number of Repairs: 0"""
        self.assertEqual(expected, str(self.secondhand_car))

if __name__ == "__main__":
    main()