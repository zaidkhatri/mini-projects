from book import Book
from person import Person


class Member(Person):

    MAX_BOOKS_ALLOWED = 3

    def __init__(self, name, age, member_id):
        super().__init__(name, age)
        self._member_id = member_id
        self._borrowed_books = []

    @property
    def member_id(self):
        return self._member_id

    @property
    def borrowed_books(self):
        return list(self._borrowed_books)

    def borrow_book(self, book: Book):
        if len(self._borrowed_books) >= self.MAX_BOOKS_ALLOWED:
            print(f"{self._name} cannot borrow more than {self.MAX_BOOKS_ALLOWED} books.")
            return False
        try:
            book.mark_as_borrowed()
        except ValueError as e:
            print(e)
            return False
        self.borrowed_books.append(book)
        print(f"{self._name} borrowed {book.title}")
        return True

    def return_book(self, book: Book):
        if book not in self._borrowed_books:
            print(f"{self._name} did not borrow {book.title}")
            return False
        book.mark_as_returned()
        self._borrowed_books.remove(book)
        print(f"{self._name} returned {book.title}.")
        return True

    def introduce_yourself(self):
        return f"Hi, I'm {self._name}, a library member (ID: {self._member_id})."
 
    def __str__(self):
        return f"Member: {self._name} (ID: {self._member_id}) - {len(self._borrowed_books)} book(s) borrowed"
        
