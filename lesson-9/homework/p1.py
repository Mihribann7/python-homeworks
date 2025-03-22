class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise Exception("Member not found.")

        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found.")

        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book '{book_title}' is already borrowed.")

        if len(member.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"Member '{member_name}' can't borrow more than 3 books.")

        book.is_borrowed = True
        member.borrowed_books.append(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise Exception("Member not found.")

        book = next((b for b in member.borrowed_books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(f"Book '{book_title}' was not borrowed by '{member_name}'.")

        book.is_borrowed = False
        member.borrowed_books.remove(book)

library = Library()

library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

library.add_member(Member("Alice"))

try:
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "Nonexistent Book")
except Exception as e:
    print(e)

try:
    library.borrow_book("Alice", "The Great Gatsby")
    library.borrow_book("Alice", "Brave New World")
except Exception as e:
    print(e)

try:
    library.return_book("Alice", "1984")

    library.return_book("Alice", "The Great Gatsby")
except Exception as e:
    print(e)
