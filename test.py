
class Book:
    def __init__(self, title: str, author: str, year: int, status: bool):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.id = self.year + str(len(self.title)) + str(len(self.author)) + str(status)

    def __str__(self):
        return f"ID: {self.id} - {self.title} ({self.year}) - {self.author}. Status: {self.status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book_id == book.id:
                self.books.remove(book)
            else:
                print("No book found")

    def get_books(self):
        if not self.books:
            print("No books found")
        else:
            for book in self.books:
                print(book)


    def search_book(self, request):
        for book in self.books:
            if request in "".join([book.title, book.author, book.year, book.title.lower(), book.author.lower(), book.year.lower()]):
                print(book)
            else:
                print("No book found")

    def update_status(self, book_id, status: bool):
        for book in self.books:
            if book_id == book.id:
                book.status = status
            else:
                print("No book found")


if __name__ == "__main__":
    library = Library()
    while True:
        print("1. Add book")
        print("2. Remove book")
        print("3. Get books")
        print("4. Search book")
        print("5. Update book status")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            status = input("Enter status: ")
            book = Book(title, author, year, status)
            library.add_book(book)
        elif choice == "2":
            book_id = input("Enter book id: ")
            library.remove_book(book_id)
        elif choice == "3":
            library.get_books()
        elif choice == "4":
            string = input("Enter search string: ")
            library.search_book(string)
        elif choice == "5":
            book_id = input("Enter book id: ")
            status = input("Enter status: ")
            library.update_status(book_id, status)
        elif choice == "6":
            break
        else:
            print("Invalid choice")