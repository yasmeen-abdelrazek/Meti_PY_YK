class Book:
    def __init__(self, title, author, availability=True):
        self.title = title
        self.author = author
        self.availability = availability  
    
    def check_out(self):
        if self.availability:
            self.availability = False
            print(f"The book '{self.title}' has been checked out.")
        else:
            print(f"The book '{self.title}' is currently unavailable.")
    
    def return_book(self):
        if not self.availability:
            self.availability = True
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not checked out.")
    
    def display_info(self):
        availability_status = "Available" if self.availability else "Checked out"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {availability_status}")

class LibraryCatalogue:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, availability=True):
        new_book = Book(title, author, availability)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the catalogue.")
    
    def display_all_books(self):
        if not self.books:
            print("No books in the catalogue.")
            return
        for book in self.books:
            book.display_info()
            print("-" * 40)

# Create new library catalogue
library = LibraryCatalogue()

# Add books to the catalogue
library.add_book("To Kill a Mockingbird", "Harper Lee", True)
library.add_book("1984", "George Orwell", True)
library.add_book("Moby Dick", "Herman Melville", False)

# Display all books in the catalogue
print("\nDisplaying all books in the catalogue:")
library.display_all_books()

# Check out  book
print("\nChecking out 'To Kill a Mockingbird':")
library.books[0].check_out()

# Try to check out the same book again
print("\nTrying to check out 'To Kill a Mockingbird' again:")
library.books[0].check_out()

# Return a book
print("\nReturning 'To Kill a Mockingbird':")
library.books[0].return_book()

# Display all books again
print("\nDisplaying all books after return:")
library.display_all_books()
