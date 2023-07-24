from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(4.5, 10.0)

    def test_default_fuel_consumption_class_attribute(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_initialize_vehicle(self):
        self.assertEqual(4.5, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(10.0, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_with_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.assertEqual(4.5, self.vehicle.fuel)
        self.vehicle.drive(2)
        self.assertEqual(2, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(5)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_enough_fuel(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(2)
        self.assertEqual(3, self.vehicle.fuel)

    def test_str_represent_class_instance(self):
        expected = "The vehicle has 10.0 horse power with 4.5 fuel left and 1.25 fuel consumption"
        result = str(self.vehicle)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()