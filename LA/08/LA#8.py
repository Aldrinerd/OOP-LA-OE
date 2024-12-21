class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
book1 = Book("Naruto", "Kishimoto")
print(book1.title, book1.author)
del book1.author
#print(book1.author) - temporarily removed since I want to check if removing an attribute doesn't affect other objects
book2 = Book("Titanic", "James Cameron")
print(book2.author)
