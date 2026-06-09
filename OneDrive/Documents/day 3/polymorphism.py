class Book:
    def show(self):
        print("Library Book")

class EBook:
    def show(self):
        print("Digital Book")

for item in [Book(), EBook()]:
    item.show()