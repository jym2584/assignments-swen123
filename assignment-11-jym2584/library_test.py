from library import *
import io

def test_book():
    # setup
    author = "JK Rowling"
    title = "Lord of the Ring"

    #Invoke
    book = Book(title, author)

    assert title == book.title
    assert author == book.author
    assert 1 == book.copies