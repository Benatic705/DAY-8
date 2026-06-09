class Book:
    def __init__(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

book = Book("Python Basics")
print(book.get_title())