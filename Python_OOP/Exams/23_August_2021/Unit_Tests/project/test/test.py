from unittest import TestCase, main
from project.library import Library

class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library("Ivan Vazov")

    def test_initialize_library_instances(self):
        self.assertEqual("Ivan Vazov", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_add_empty_name_to_library_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_set_name_to_library(self):
        self.library.name = "Hristo Botev"
        self.assertEqual("Hristo Botev", self.library.name)

    def test_add_book_not_existing_author_and_title_in_the_library(self):
        self.library.add_book("Aleko Konstantinov", "Bai Ganio")
        self.assertEqual({"Aleko Konstantinov": ["Bai Ganio"]}, self.library.books_by_authors)

    def test_add_book_with_existing_author_and_not_existing_title_in_the_library(self):
        self.library.books_by_authors["Aleko Konstantinov"] = []
        self.library.add_book("Aleko Konstantinov", "Bai Ganio")
        self.assertEqual({"Aleko Konstantinov": ["Bai Ganio"]}, self.library.books_by_authors)

    def test_add_book_with_existing_author_and_existing_title_in_the_library(self):
        self.library.books_by_authors["Aleko Konstantinov"] = ["Bai Ganio"]
        self.library.add_book("Aleko Konstantinov", "Bai Ganio")
        self.assertEqual({"Aleko Konstantinov": ["Bai Ganio"]}, self.library.books_by_authors)

    def test_add_reader_registered_in_the_library_already(self):
        self.library.readers["Ivan"] = []
        result = self.library.add_reader("Ivan")
        self.assertEqual("Ivan is already registered in the Ivan Vazov library.", result)

    def test_add_reader_in_the_library_allowed(self):
        self.library.add_reader("Ivan")
        self.assertEqual({"Ivan": []}, self.library.readers)

    def test_rent_book_if_reader_name_not_in_library(self):
        result = self.library.rent_book("Ivan", "Aleko Konstantinov", "Bai Ganio")
        self.assertEqual("Ivan is not registered in the Ivan Vazov Library.", result)

    def test_rent_book_if_book_author_not_in_library(self):
        self.library.readers["Ivan"] = []
        result = self.library.rent_book("Ivan", "Aleko Konstantinov", "Bai Ganio")
        self.assertEqual("Ivan Vazov Library does not have any Aleko Konstantinov's books.", result)

    def test_rent_book_if_book_title_not_in_library(self):
        self.library.readers["Ivan"] = []
        self.library.books_by_authors["Aleko Konstantinov"] = []
        result = self.library.rent_book("Ivan", "Aleko Konstantinov", "Bai Ganio")
        self.assertEqual("""Ivan Vazov Library does not have Aleko Konstantinov's "Bai Ganio".""", result)

    def test_rent_book_from_library_allowed(self):
        self.library.readers["Ivan"] = []
        self.library.books_by_authors["Aleko Konstantinov"] = ["Bai Ganio"]
        result = self.library.rent_book("Ivan", "Aleko Konstantinov", "Bai Ganio")
        self.assertEqual({"Ivan": [{"Aleko Konstantinov": "Bai Ganio"}]}, self.library.readers)
        self.assertEqual({"Aleko Konstantinov": []}, self.library.books_by_authors)


if __name__ == "__main__":
    main()