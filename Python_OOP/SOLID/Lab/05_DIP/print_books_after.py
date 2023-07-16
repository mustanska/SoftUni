class Book:
    def __init__(self, name: str, author: str, content: str):
        self.name = name
        self.author = author
        self.content = content


class Formatter:
    @staticmethod
    def format(book: Book) -> str:
        return f"{book.name}\n{book.author}\n{book.content}"


class Printer:
    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)


book = Book("Bai Ganio", "Aleko Konstantinov", "...")
printer = Printer(Formatter())
print(printer.get_book(book))