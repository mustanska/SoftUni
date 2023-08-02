from unittest import TestCase, main
from project.robot import Robot

class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot  = Robot("id_1", "Military", 10, 5.5)

    def test_robot_class_attributes(self):
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], self.robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, self.robot.PRICE_INCREMENT)

    def test_initialize_robot(self):
        self.assertEqual("id_1", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(5.5, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_not_allowed_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Robots"

        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'",
                         str(ve.exception))

    def test_negative_price_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_robot(self):
        result = self.robot.upgrade("sensor", 3)
        self.assertEqual(["sensor"], self.robot.hardware_upgrades)
        self.assertEqual(10, self.robot.price)
        self.assertEqual("Robot id_1 was upgraded with sensor.", result)

        result = self.robot.upgrade("sensor", 4)
        self.assertEqual("Robot id_1 was not upgraded.", result)

    def test_update_robot(self):
        result = self.robot.update(1.2, 2)
        self.assertEqual([1.2], self.robot.software_updates)
        self.assertEqual(8, self.robot.available_capacity)
        self.assertEqual("Robot id_1 was updated to version 1.2.", result)

        result = self.robot.update(1.1, 3)
        self.assertEqual("Robot id_1 was not updated.", result)

        result = self.robot.update(1.3, 11)
        self.assertEqual("Robot id_1 was not updated.", result)

    def test_greater_than(self):
        other = Robot("id_2", "Education", 10, 5)
        result = self.robot > other
        self.assertEqual("Robot with ID id_1 is more expensive than Robot with ID id_2.", result)

        other.price += 0.5
        result = self.robot > other
        self.assertEqual("Robot with ID id_1 costs equal to Robot with ID id_2.", result)

        other.price += 0.5
        result = self.robot > other
        self.assertEqual("Robot with ID id_1 is cheaper than Robot with ID id_2.", result)


if __name__ == "__main__":
    main()
