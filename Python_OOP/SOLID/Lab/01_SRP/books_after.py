class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        try:
            book = [b for b in self.books if b.title == title][0]
            return f'The book "{book.title}" with author {book.author} is in the library "{self.name}".'
        except IndexError:
            return f'There is no book with title "{title}"!'


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


library = Library("Ivan Vazov")
book1 = Book("Bai Ganio", "Aleko Konstantinov")
library.add_book(book1)
print(library.find_book("Bai Ganio"))
print(library.find_book("Nemili nedragi"))
