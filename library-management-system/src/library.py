from book import Book
from member import Member

class Library:
    def __init__(self, name):
        self._name = name
        self._books = []
        self._members = []

    def add_book(self, book: Book):
        self._books.append(book)

    def remove_book(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                self._books.remove(book)
                return book
        print(f"No book found with ISBN {isbn}.")
        return None
 
    def register_member(self, member: Member):
        self._members.append(member)
        print(f"Registered new member: {member.name}")
 
    def find_book(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None
 
    def list_available_books(self):
        print(f"\n--- Available books at {self._name} ---")
        available = [b for b in self._books if b.is_available]
        if not available:
            print("No books currently available.")
        for book in available:
            print(f"  {book}")
 
    def list_all_books(self):
        print(f"\n--- Full catalog at {self._name} ---")
        for book in self._books:
            print(f"  {book}")