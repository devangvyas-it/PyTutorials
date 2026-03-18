# Defining the Class (The Blueprint)
class Book:
    def __init__(self, title, author, isbn):
        # Attributes (Data)
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    # Method (Behavior)
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return f"Success! You borrowed '{self.title}'."
        return f"Sorry, '{self.title}' is currently unavailable."

    def return_book(self):
        self.is_available = True
        return f"Thank you for returning '{self.title}'."

# Creating Objects (Instances of the Blueprint)
book1 = Book("Python Basics", "Guido van Rossum", "123-456")
book2 = Book("Algorithm Master", "Ada Lovelace", "789-012")

# interacting with the objects
print(book1.borrow_book())
print(book1.borrow_book()) # Trying to borrow it again
print(book1.return_book())