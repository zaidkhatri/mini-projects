from book import Book
from person import Person


class Librarian(Person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self._staff_id = staff_id

    @property
    def staff_id(self):
        return self._staff_id

    def add_book_to_library(self, library, book: Book):
        library.add_book(book)
        print(f"Librarian {self._name} added '{book.title}' to the library.")
 
    def remove_book_from_library(self, library, isbn):
        removed = library.remove_book(isbn)
        if removed:
            print(f"Librarian {self._name} removed '{removed.title}' from the library.")
 
    # --- POLYMORPHISM: a different override of the same method name ---
    def introduce_yourself(self):
        return f"Hi, I'm {self._name}, the librarian (Staff ID: {self._staff_id})."
 
    def __str__(self):
        return f"Librarian: {self._name} (Staff ID: {self._staff_id})"