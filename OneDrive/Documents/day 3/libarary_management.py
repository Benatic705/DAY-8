class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

book1 = Book("Python Programming", "Benatic")
book2 = Book("OOP Concepts", "Rithan")

print("Library Books")
print("-------------")
book1.display()
print()
book2.display()