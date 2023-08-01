from unittest import TestCase, main
from project.truck_driver import TruckDriver

class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.truck_driver = TruckDriver("Name", 5)

    def test_initialize_truck_driver(self):
        self.assertEqual("Name", self.truck_driver.name)
        self.assertEqual(5, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_earned_money_is_less_than_zero_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -1
        self.assertEqual("Name went bankrupt.", str(ve.exception))

    def test_add_cargo_offer(self):
        result = self.truck_driver.add_cargo_offer("somewhere", 20)
        self.assertEqual({"somewhere": 20}, self.truck_driver.available_cargos)
        self.assertEqual("Cargo for 20 to somewhere was added as an offer.", result)

        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("somewhere", 30)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_drive_best_cargo_offer(self):
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

        self.truck_driver.add_cargo_offer("somewhere", 10000)
        self.truck_driver.add_cargo_offer("anywhere", 2000)

        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(38250, self.truck_driver.earned_money)
        self.assertEqual(10000, self.truck_driver.miles)
        self.assertEqual("Name is driving 10000 to somewhere.", result)

    def test_represent_truck_driver(self):
        self.truck_driver.add_cargo_offer("anywhere", 10000)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("Name has 10000 miles behind his back.", self.truck_driver.__repr__())

if __name__ == "__main__":
    main()