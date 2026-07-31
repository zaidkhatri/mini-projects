from book import Book
from member import Member
from librarian import Librarian
from library import Library
 
 
def main():
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM — OOP DEMO")
    print("=" * 60)
 
    # Create the library
    library = Library("Community Library")
 
    # Create a librarian and some books
    librarian = Librarian("Asha Patel", 34, staff_id="LIB001")
 
    book1 = Book("The Hobbit", "J.R.R. Tolkien", "ISBN001")
    book2 = Book("Clean Code", "Robert C. Martin", "ISBN002")
    book3 = Book("Dune", "Frank Herbert", "ISBN003")
 
    librarian.add_book_to_library(library, book1)
    librarian.add_book_to_library(library, book2)
    librarian.add_book_to_library(library, book3)
 
    # Create members
    member1 = Member("Rahul Shah", 21, member_id="MEM001")
    member2 = Member("Priya Mehta", 25, member_id="MEM002")
 
    library.register_member(member1)
    library.register_member(member2)
 
    library.list_available_books()
 
    # --- POLYMORPHISM in action ---
    # Same method call, different behavior depending on the object's actual class.
    print("\n--- Everyone introduces themselves (polymorphism) ---")
    people = [librarian, member1, member2]
    for person in people:
        print(person.introduce_yourself())
 
    # --- Borrowing and returning books ---
    print("\n--- Borrowing books ---")
    member1.borrow_book(book1)
    member1.borrow_book(book2)
    member2.borrow_book(book1)  # should fail, already borrowed
 
    library.list_available_books()
 
    print("\n--- Returning a book ---")
    member1.return_book(book1)
 
    library.list_available_books()
 
    # --- Librarian removes a book ---
    print("\n--- Librarian removes a book ---")
    librarian.remove_book_from_library(library, "ISBN003")
 
    library.list_all_books()
 
    # --- Printing objects directly uses __str__ (also polymorphism) ---
    print("\n--- Member and Librarian summaries ---")
    print(member1)
    print(member2)
    print(librarian)
 
 
if __name__ == "__main__":
    main()