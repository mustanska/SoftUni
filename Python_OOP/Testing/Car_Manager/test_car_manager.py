import unittest

from Testing.Car_Manager.car_manager import Car


class CarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("a", "b", 1, 4)

    def test_initialize_car(self):
        self.assertEqual("a", self.car.make)
        self.assertEqual("b", self.car.model)
        self.assertEqual(1, self.car.fuel_consumption)
        self.assertEqual(4, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.make = None

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_setter(self):
        self.assertEqual("a", self.car.make)
        self.car.make = "new_a"
        self.assertEqual("new_a", self.car.make)

    def test_model_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.model = None

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_setter(self):
        self.assertEqual("b", self.car.model)
        self.car.model = "new_b"
        self.assertEqual("new_b", self.car.model)

    def test_fuel_consumption_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_setter(self):
        self.assertEqual(1, self.car.fuel_consumption)
        self.car.fuel_consumption = 2
        self.assertEqual(2, self.car.fuel_consumption)

    def test_fuel_capacity_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter(self):
        self.assertEqual(4, self.car.fuel_capacity)
        self.car.fuel_capacity = 5
        self.assertEqual(5, self.car.fuel_capacity)

    def test_fuel_amount_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_setter(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.fuel_amount = 5
        self.assertEqual(5, self.car.fuel_amount)

    def test_refuel_car_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_car(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(1)
        self.assertEqual(1, self.car.fuel_amount)

        self.car.refuel(5)
        self.assertEqual(4, self.car.fuel_amount)

    def test_drive_car_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(20)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_car(self):
        self.car.fuel_amount = 1
        self.car.drive(50)
        self.assertEqual(0.5, self.car.fuel_amount)


if __name__ == '__main__':
    unittest.main()
