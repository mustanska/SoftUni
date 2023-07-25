from unittest import TestCase, main
from project.pet_shop import PetShop

class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("Pet Shop")

    def test_initialize_pet_shop_instance(self):
        self.assertEqual("Pet Shop", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_to_pet_shop_with_quantity_equal_to_zero_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("meat", 0)

        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))

    def test_add_food_to_pet_shop_with_quantity_less_than_zero_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("meat", -1)

        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))

    def test_add_food_to_pet_shop_that_not_existed(self):
        result = self.pet_shop.add_food("meat", 1)
        self.assertEqual({"meat": 1}, self.pet_shop.food)
        self.assertEqual("Successfully added 1.00 grams of meat.", result)

    def test_add_food_to_pet_shop_with_existing_food(self):
        self.pet_shop.food = {"meat": 1}
        result = self.pet_shop.add_food("meat", 1)
        self.assertEqual({"meat": 2}, self.pet_shop.food)
        self.assertEqual("Successfully added 1.00 grams of meat.", result)

    def test_add_pet_to_pet_shop_if_pet_is_already_exist_raises(self):
        self.pet_shop.pets = ["Sharo"]
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Sharo")

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_to_pet_shop_allowed(self):
        result = self.pet_shop.add_pet("Sharo")
        self.assertEqual(["Sharo"], self.pet_shop.pets)
        self.assertEqual("Successfully added Sharo.", result)

    def test_feed_pet_from_pet_shop_when_pet_does_not_exist_raises(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("meat", "Sharo")

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_from_pet_shop_when_food_does_not_exist(self):
        self.pet_shop.pets = ["Sharo"]
        result = self.pet_shop.feed_pet("meat", "Sharo")
        self.assertEqual("You do not have meat", result)

    def test_feed_pet_from_pet_shop_when_quantity_of_food_is_less_than_100(self):
        self.pet_shop.food["meat"] = 90
        self.pet_shop.pets = ["Sharo"]
        result = self.pet_shop.feed_pet("meat", "Sharo")
        self.assertEqual({"meat": 1090}, self.pet_shop.food)
        self.assertEqual("Adding food...", result)

    def test_feed_pet_from_pet_shop_allowed(self):
        self.pet_shop.food["meat"] = 250
        self.pet_shop.pets = ["Sharo"]
        result = self.pet_shop.feed_pet("meat", "Sharo")
        self.assertEqual({"meat": 150}, self.pet_shop.food)
        self.assertEqual("Sharo was successfully fed", result)

    def test_represent_pet_shop_instances_without_pets(self):
        expected =f"Shop Pet Shop:\nPets: "
        self.assertEqual(expected, str(self.pet_shop))

    def test_represent_pet_shop_instances_with_pets(self):
        self.pet_shop.pets = ["Sharo", "Ares"]
        expected =f"Shop Pet Shop:\nPets: Sharo, Ares"
        self.assertEqual(expected, str(self.pet_shop))

if __name__ == "__main__":
    main()