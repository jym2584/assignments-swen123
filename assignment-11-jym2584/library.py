import csv

class Book:
    __slots__ = ["title", "author", "copies"]
    
    def __init__ (self, title, author, copies = 1):
        self.title = title
        self.author = author
        self.copies = copies

class Patron:
    __slots__ = ["id", "name", "wants", "has"]

    def __init__ (self, id, name):
        self.id = id
        self.name = name
        self.wants = set()
        self.has = set()

class CardCatalog:
    __slots__ = ["books_by_author", "books_by_title"]
    
    def __init__ (self):
        self.books_by_author = {}
        self.books_by_title = {}

class Library:
    __slots__ = ['patrons', 'shelves', 'card_catalog']

    def __init__ (self, filename):
        self.patrons = {}
        self.shelves = []
        self.card_catalog = CardCatalog()

        with open(filename) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for record in csv_reader:
                title = record[0]
                author = record[1]
                copies = record[2]
                book = Book(title, author, copies)
                self.shelves.append(book)

                by_author = self.card_catalog.books_by_author
                if author not in by_author:
                    by_author[author] = []
                by_author[author] += [book]

                by_title = self.card_catalog.books_by_title
                if title not in by_title:
                    by_title[title] = []
                by_title[title] += [book]

LIBRARY = Library('books.csv')

def find_by_author(author):
    books = []
    if author in LIBRARY.card_catalog.books_by_author:
        books = LIBRARY.card_catalog.books_by_author[author]
    
    return books

def find_by_title(title):
    books = []
    if title in LIBRARY.card_catalog.books_by_title:
        books = LIBRARY.card_catalog.books_by_title[title]
    
    return books

def checkout(book, patron):
    if book.copies > 0:
        patron.has.add(book)
        book.copies -= 1
    else:
        patron.wants.add(book)

def return_book(book, patron):
    book.copies += 1
    patron.has.remove(book)
    for patron in LIBRARY.patrons:
        if book in patron.wants:
            checkout(book, patron)
            break

def main():
    books = find_by_author("Saul Bellow")
    print(books)

if __name__ == "__main__":
    main()