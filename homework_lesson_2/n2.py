from collections import namedtuple

Book = namedtuple("Book",["title", "author", "year", "price"])

books = (
    Book("Clean Code", "Robert C. Martin", 2008, "$35"),
    Book("The Pragmatic", "Andrew Hunt, David Thomas", 1999, "$40"),
    Book("Introduction to Algorithms", "Thomas H.", 2009, "$80"),
    Book("Python Crash Course", "Eric Matthes", 2015, "$25"),
    Book("Design Patterns", "Erich Gamma", 1994, "$50")
)

for x in books:
    if x.year > 2010:
        print(f"title: {x.title}, price: {x.price}")