import pytest
from unittest.mock import Mock
from library_manager import LibraryManager

@pytest.fixture
def library_manager():
    return LibraryManager()

def test_add_book_success(library_manager):
    library_manager.add_book(1, "1984", "George Orwell")
    assert len(library_manager.books) == 1

def test_add_book_duplicate_id(library_manager):
    library_manager.add_book(1, "1984", "George Orwell")
    with pytest.raises(ValueError, match="Book ID already exists"):
        library_manager.add_book(1, "Animal Farm", "George Orwell")

def test_get_book_success(library_manager):
    library_manager.add_book(1, "1984", "George Orwell")
    book = library_manager.get_book(1)
    assert book["title"] == "1984"
    assert book["author"] == "George Orwell"

def test_get_book_not_found(library_manager):
    with pytest.raises(ValueError, match="Book not found"):
        library_manager.get_book(99)

def test_remove_book_success(library_manager):
    library_manager.add_book(1, "1984", "George Orwell")
    library_manager.remove_book(1)
    assert len(library_manager.books) == 0

def test_remove_book_not_found(library_manager):
    with pytest.raises(ValueError, match="Book not found"):
        library_manager.remove_book(99)

def test_list_books(library_manager):
    library_manager.add_book(1, "1984", "George Orwell")
    library_manager.add_book(2, "Brave New World", "Aldous Huxley")
    books = library_manager.list_books()
    assert len(books) == 2
    assert books[0]["title"] == "1984"
    assert books[1]["title"] == "Brave New World"

def test_mock_add_book():
    mock_manager = Mock(spec=LibraryManager)
    mock_manager.add_book.return_value = None
    mock_manager.add_book(1, "1984", "George Orwell")
    mock_manager.add_book.assert_called_once_with(1, "1984", "George Orwell")
