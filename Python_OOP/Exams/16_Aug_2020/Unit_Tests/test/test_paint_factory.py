from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory("Test", 50)

    def test_initialize_paint_factory_class_instance(self):
        self.assertEqual("Test", self.paint_factory.name)
        self.assertEqual(50, self.paint_factory.capacity)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)

    def test_can_add_to_paint_factory_is_true(self):
        self.paint_factory.ingredients["white"] = 10
        result = self.paint_factory.can_add(10)
        self.assertTrue(result)

    def test_can_add_to_paint_factory_is_false(self):
        self.paint_factory.ingredients["white"] = 50
        result = self.paint_factory.can_add(10)
        self.assertFalse(result)

    def test_add_ingredient_to_paint_factory_not_valid_ingredient(self):
        with self.assertRaises(TypeError) as te:
            self.paint_factory.add_ingredient("orange", 20)

        self.assertEqual("Ingredient of type orange not allowed in PaintFactory", str(te.exception))

    def test_add_ingredient_to_paint_factory_not_enough_capacity_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.paint_factory.add_ingredient("yellow", 60)

        self.assertEqual("Not enough space in factory", str(ve.exception))

    def test_add_ingredient_to_paint_factory_with_added_new_ingredient_and_quantity(self):
        self.paint_factory.add_ingredient("white", 10)
        self.assertEqual(10, self.paint_factory.ingredients["white"])

    def test_add_ingredient_to_paint_factory_with_added_quantity_to_existing_ingredient(self):
        self.paint_factory.ingredients["white"] = 10
        self.paint_factory.add_ingredient("white", 10)
        self.assertEqual(20, self.paint_factory.ingredients["white"])

    def test_remove_ingredient_from_paint_factory_not_existing_ingredient_raises(self):
        with self.assertRaises(KeyError) as ke:
            self.paint_factory.remove_ingredient("white", 10)

        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))

    def test_remove_ingredient_from_paint_factory_less_than_zero_raises(self):
        self.paint_factory.ingredients["white"] = 10

        with self.assertRaises(ValueError) as ve:
            self.paint_factory.remove_ingredient("white", 20)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))

    def test_remove_ingredient_from_paint_factory_allowed(self):
        self.paint_factory.ingredients["white"] = 10
        self.paint_factory.remove_ingredient("white", 5)
        self.assertEqual(5, self.paint_factory.ingredients["white"])

    def test_property_products_with_empty_ingredients_list(self):
        self.assertEqual({}, self.paint_factory.products)

    def test_property_products_with_ingredients_in_list(self):
        self.paint_factory.ingredients = {"white": 10, "blue": 20}
        self.assertEqual({"white": 10, "blue": 20}, self.paint_factory.products)

    def test_represent_paint_factory_instance_without_ingredients(self):
        self.assertEqual("Factory name: Test with capacity 50.\n", str(self.paint_factory))

    def test_represent_paint_factory_instance_with_ingredients(self):
        self.paint_factory.ingredients = {"white": 10, "blue": 20}
        excepted = "Factory name: Test with capacity 50.\nwhite: 10\nblue: 20\n"
        self.assertEqual(excepted, str(self.paint_factory))

if __name__ == "__main__":
    main()
