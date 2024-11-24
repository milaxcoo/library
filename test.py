
class Book:
    """Класс, представляющий книгу."""
    def __init__(self, title: str, author: str, year: int, status: bool):
        """
        Инициализирует объект книги.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания.
        :param status: Статус книги ("в наличии" или "выдана").
        """
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.id = self.year + str(len(self.title)) + str(len(self.author)) + str(status)

    def __str__(self):
        """
        Возвращает строковое представление книги.
        :return: Строка с информацией о книге.
        """
        return f"ID: {self.id} - {self.title} ({self.year}) - {self.author}. Status: {self.status}"


class Library:
    """Класс управления библиотекой."""
    def __init__(self):
        """Инициализирует пустую библиотеку."""
        self.books = []

    def add_book(self, book):
        """
        Добавляет книгу в библиотеку.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания.
        """
        self.books.append(book)

    def remove_book(self, book_id):
        """
        Удаляет книгу из библиотеки по её ID.
        :param book_id: Уникальный идентификатор книги.
        """
        for book in self.books:
            if book_id == book.id:
                self.books.remove(book)
            else:
                print("No book found")

    def get_books(self):
        """
        Отображает все книги в библиотеке.
        """
        if not self.books:
            print("No books found")
        else:
            for book in self.books:
                print(book)


    def search_book(self, request):
        """
        Ищет книги в библиотеке по названию или автору.
        :param request: Строка для поиска.
        """
        for book in self.books:
            if request in "".join([book.title, book.author, book.year, book.title.lower(), book.author.lower(), book.year.lower()]):
                print(book)
            else:
                print("No book found")

    def update_status(self, book_id, status_: bool):
        """
        Обновляет статус книги.
        :param book_id: Уникальный идентификатор книги.
        :param status_: Новый статус книги типа bool ("в наличии" или "выдана").
        """
        for book in self.books:
            if book_id == book.id:
                book.status = status
            else:
                print("No book found")


if __name__ == "__main__":
    """Основная функция, реализующая консольное меню управления библиотекой."""
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
