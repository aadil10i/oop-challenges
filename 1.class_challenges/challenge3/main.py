# main handles instances initialization and method calling
def main():
    # Creating Book objects
    book1 = Book("The Cat in the Hat", "Dr. Seuss")
    book2 = Book("The Hobbit", "J.R.R. Tolkien")
    book3 = Book("Pride and Prejudice", "Jane Austen")

    # Creating a Library object
    my_library = Library("Aadil's Great Library")

    # Adding books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    print(f"Books in {my_library.name}:")
    for book in my_library.books:
        print(f"- {book.title} by {book.author}")

    # Removing a book
    my_library.remove_book(book1)

    print("\nAfter removing a book:")
    for book in my_library.books:
        print(f"- {book.title} by {book.author}")

    # Searching for books
    search_term = "Pr"
    search_results = my_library.search_books(search_term)
    print(f"\nSearch results for '{search_term}':")
    for book in search_results:
        print(f"- {book.title} by {book.author}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    # these methods access library book because it's initialized in their same constructor
    # accesses the book from Book class, through parameters set by instances in main func
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_to_remove):
        for library_book in self.books: # Iterate over a copy to allow removal
            if library_book.title == book_to_remove.title and library_book.author == book_to_remove.author:
                self.books.remove(library_book)
                break

    def search_books(self, search_string):
        returned_books = []
        for library_book in self.books:
            if (search_string.lower() in library_book.title.lower() 
                or search_string.lower() in library_book.author.lower()):

                returned_books.append(library_book)
        
        return returned_books

main()
