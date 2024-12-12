class LibraryManager:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author):
        if any(book["book_id"] == book_id for book in self.books):
            raise ValueError("Book ID already exists")
        self.books.append({"book_id": book_id, "title": title, "author": author})

    def get_book(self, book_id):
        for book in self.books:
            if book["book_id"] == book_id:
                return book
        raise ValueError("Book not found")

    def remove_book(self, book_id):
        for book in self.books:
            if book["book_id"] == book_id:
                self.books.remove(book)
                return
        raise ValueError("Book not found")

    def list_books(self):
        return self.books
