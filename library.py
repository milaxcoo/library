class Book:
    """Класс, представляющий книгу."""
    def __init__(self, title: str, author: str, year: int, status: bool) -> None:
        """
        Инициализирует объект книги.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания.
        :param status: Статус книги ("в наличии" или "выдана").
        :param id: Уникальный идентификатор книги.
        """
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.id = self.year + str(len(self.title)) + str(len(self.author)) + str(status)

    def to_text(self) -> str:
        """
        Преобразует объект книги в строку для сохранения в текстовом файле.
        :return: Строка в формате "id|title|author|year|status".
        """
        return f"{self.id}|{self.title}|{self.author}|{self.year}|{self.status}"

    def from_text(line: str) -> "Book":
        """
        Создаёт объект книги из строки.
        :param line: Строка в формате "id|title|author|year|status".
        :return: Объект Book.
        """
        parts = line.strip().split("|")
        return Book(parts[1], parts[2], parts[3], parts[4])

    
    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.
        """
        return f"ID: {self.id} - {self.title} ({self.year}) - {self.author}. Status: {self.status}"


class Library:
    """Класс управления библиотекой."""
    def __init__(self, file: str = "library.txt") -> None:
        """
        Инициализирует библиотеку с загрузкой данных из файла.
        :param file: Имя файла для хранения данных.
        """
        self.books = []
        self.file = file
        self.load_books()

    def save_books(self) -> None:
        """Сохраняет книги в текстовый файл."""
        try:
            with open(self.file, "w", encoding="utf-8") as f:
                for book in self.books:
                    f.write(book.to_text() + "\n")
            print("Данные сохранены.")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

    def load_books(self) -> None:
        """Загружает книги из текстового файла."""
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                self.books = [Book.from_text(line) for line in f]
            print("Данные успешно загружены.")
        except FileNotFoundError:
            print("Файл с данными не найден. Будет создан новый.")
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")


    def add_book(self, book) -> None:
        """
        Добавляет книгу в библиотеку.
        """
        self.books.append(book)
        self.save_books()

    def remove_book(self, book_id) -> None:
        """
        Удаляет книгу из библиотеки по её ID.
        :param book_id: Уникальный идентификатор книги.
        """
        for book in self.books:
            if book_id == book.id:
                self.books.remove(book)
            else:
                print("No book found")

    def get_books(self) -> None:
        """
        Отображает все книги в библиотеке.
        """
        if not self.books:
            print("No books found")
        else:
            for book in self.books:
                print(book)


    def search_book(self, request) -> None:
        """
        Ищет книги в библиотеке по названию или автору.
        :param request: Строка для поиска.
        """
        for book in self.books:
            if request in "".join([book.title, book.author, book.year, book.title.lower(), book.author.lower(), book.year.lower()]):
                print(book)
            else:
                print("No book found")

    def update_status(self, book_id, status_: bool) -> None:
        """
        Обновляет статус книги.
        :param book_id: Уникальный идентификатор книги.
        :param status_: Новый статус книги типа bool ("в наличии" или "выдана").
        """
        for book in self.books:
            if book_id == book.id:
                book.status = status_
            else:
                print("No book found")


if __name__ == "__main__":
    """Основная функция, реализующая консольное меню управления библиотекой."""
    library = Library()

    while True:
        print("\n1. Add book")
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
