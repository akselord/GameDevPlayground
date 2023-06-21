class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        availability = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} ({availability})"


class Library:
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)
        print("Book added to the library.")

    def borrow_book(self, title):
        for book in self.catalog:
            if book.title == title and book.available:
                book.available = False
                print("Book borrowed successfully.")
                return
        print("Book not found or not available for borrowing.")

    def display_catalog(self):
        if self.catalog:
            print("Library Catalog:")
            for book in self.catalog:
                print(book)
        else:
            print("No books in the library catalog.")

# Usage example
library = Library()

book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_catalog()

library.borrow_book("To Kill a Mockingbird")
library.borrow_book("The Great Gatsby")

library.display_catalog()
