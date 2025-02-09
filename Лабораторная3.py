class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс для бумажных книг. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Call the setter to validate

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """ Класс для аудио книг. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Call the setter to validate

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

# Примеры использования
if __name__ == '__main__':
    paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
    audio_book = AudioBook("Гарри Поттер", "Дж.К. Роулинг", 10.5)

    print(paper_book)  # Проверяем метод __str__ для бумажной книги
    print(repr(paper_book))  # Проверяем метод __repr__ для бумажной книги

    print(audio_book)  # Проверяем метод __str__ для аудио книги
    print(repr(audio_book))  # Проверяем метод __repr__ для аудио книги

    # Пробуем задать некорректные значения для проверки ошибок
    try:
        paper_book.pages = -5  # Это вызовет ValueError
    except ValueError as e:
        print(e)

    try:
        audio_book.duration = -2.0  # Это вызовет ValueError
    except ValueError as e:
        print(e)
            