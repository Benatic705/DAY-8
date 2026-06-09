class Book:
    def __init__(self, title):
        self.title = title

class LibraryBook(Book):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

book = LibraryBook("Python Basics", "Benatic")
print(book.title)
print(book.author)