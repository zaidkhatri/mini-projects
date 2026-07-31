class Book:
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._is_available = True
    
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def is_available(self):
        return self._is_available

    def mark_as_borrowed(self):
        if not self._is_available:
            raise ValueError(f"{self._title} is already borrowed.")
        self._is_available = False

    def mark_as_returned(self):
        self._is_available = True

    def __str__(self):
        status = "Available" if self._is_available else "Borrowed"
        return f"{self._title} by {self._author} (ISBN - {self._isbn}) - {status}"