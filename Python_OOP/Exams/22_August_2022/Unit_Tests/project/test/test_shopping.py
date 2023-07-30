from unittest import TestCase, main
from project.shopping_cart import ShoppingCart

class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart("Shop", 500)

    def test_initialize_shopping_cart(self):
        self.assertEqual("Shop", self.shopping_cart.shop_name)
        self.assertEqual(500, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_shop_name_if_first_letter_is_not_upper_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "shop"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_shop_name_if_first_letter_is_not_only_letters_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "Shop123"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_if_product_price_is_more_than_or_equal_to_100_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("banana", 100)

        self.assertEqual("Product banana cost too much!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("banana", 101)

        self.assertEqual("Product banana cost too much!", str(ve.exception))

    def test_add_to_cart_successfully(self):
        self.shopping_cart.add_to_cart("apple", 20)
        result = self.shopping_cart.add_to_cart("banana", 99)
        self.assertEqual({"apple": 20, "banana": 99}, self.shopping_cart.products)
        self.assertEqual("banana product was successfully added to the cart!", result)

    def test_remove_from_cart_if_product_exist(self):
        self.shopping_cart.add_to_cart("apple", 20)
        self.shopping_cart.add_to_cart("banana", 99)
        result = self.shopping_cart.remove_from_cart("banana")
        self.assertEqual({"apple": 20}, self.shopping_cart.products)
        self.assertEqual("Product banana was successfully removed from the cart!", result)

    def test_remove_from_cart_if_product_does_not_exist_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("banana")

        self.assertEqual("No product with name banana in the cart!", str(ve.exception))

    def test_add(self):
        self.shopping_cart.add_to_cart("banana", 50)
        self.shopping_cart.add_to_cart("apple", 30)
        other = ShoppingCart("Other", 200)
        other.add_to_cart("strawberry", 40)
        new = self.shopping_cart + other
        self.assertIsInstance(new, ShoppingCart)
        self.assertEqual("ShopOther", new.shop_name)
        self.assertEqual(700, new.budget)
        self.assertEqual({"banana": 50, "apple": 30, "strawberry": 40}, new.products)

    def test_buy_products_raises(self):
        self.shopping_cart.budget = 80
        self.shopping_cart.add_to_cart("banana", 50)
        self.shopping_cart.add_to_cart("apple", 40)

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 10.00lv!", str(ve.exception))

    def test_buy_products(self):
        self.shopping_cart.add_to_cart("banana", 50)
        self.shopping_cart.add_to_cart("apple", 40)
        result = self.shopping_cart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 90.00lv.", result)

if __name__ == "__main__":
    main()

