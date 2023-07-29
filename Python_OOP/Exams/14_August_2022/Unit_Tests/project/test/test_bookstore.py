from unittest import TestCase, main
from project.bookstore import Bookstore

class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_initialize_bookstore(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_total_sold_books_method(self):
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, self.bookstore.total_sold_books)

    def test_book_limit_equal_to_zero_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_book_limit_less_than_zero_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -1

        self.assertEqual("Books limit of -1 is not valid", str(ve.exception))

    def test_len_bookstore(self):
        self.assertEqual(0, len(self.bookstore))

        self.bookstore.receive_book("Book1", 4)
        self.assertEqual(4, len(self.bookstore))

        self.bookstore.receive_book("Book2", 2)
        self.assertEqual(6, len(self.bookstore))

    def test_receive_book_if_there_is_not_enough_space_in_the_bookstore_raises(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Book", 11)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_if_there_is_enough_space_in_the_bookstore(self):
        result = self.bookstore.receive_book("Book", 5)
        self.assertEqual({"Book": 5}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual("5 copies of Book are available in the bookstore.", result)
        self.assertEqual(5, len(self.bookstore))

        result = self.bookstore.receive_book("Book", 2)
        self.assertEqual({"Book": 7}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual("7 copies of Book are available in the bookstore.", result)
        self.assertEqual(7, len(self.bookstore))
    def test_sell_book_if_the_book_is_not_available_in_the_bookstore_raises(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Book", 2)

        self.assertEqual("Book Book doesn't exist!", str(ex.exception))

    def test_sell_book_if_the_is_not_enough_copies_of_that_book_to_sell_raises(self):
        self.bookstore.receive_book("Book", 1)

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Book", 2)

        self.assertEqual("Book has not enough copies to sell. Left: 1", str(ex.exception))

    def test_sell_book(self):
        self.bookstore.receive_book("Book", 5)
        result = self.bookstore.sell_book("Book", 2)
        self.assertEqual(2, self.bookstore.total_sold_books)
        self.assertEqual(3, len(self.bookstore))
        self.assertEqual("Sold 2 copies of Book", result)

        result = self.bookstore.sell_book("Book", 3)
        self.assertEqual(5, self.bookstore.total_sold_books)
        self.assertEqual(0, len(self.bookstore))
        self.assertEqual("Sold 3 copies of Book", result)

    def test_str_bookstore_without_books_and_sold_books(self):
        expected = "Total sold books: 0\n" \
                   "Current availability: 0"
        self.assertEqual(expected, str(self.bookstore))

    def test_str_bookstore_with_books_and_sold_books(self):
        self.bookstore.receive_book("Book1", 3)
        self.bookstore.receive_book("Book2", 2)

        expected = "Total sold books: 0\n" \
                   "Current availability: 5\n" \
                   " - Book1: 3 copies\n" \
                   " - Book2: 2 copies"
        self.assertEqual(expected, str(self.bookstore))

        self.bookstore.sell_book("Book1", 2)
        expected = "Total sold books: 2\n" \
                   "Current availability: 3\n" \
                   " - Book1: 1 copies\n" \
                   " - Book2: 2 copies"
        self.assertEqual(expected, str(self.bookstore))

if __name__ == "__main__":
    main()