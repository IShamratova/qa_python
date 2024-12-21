import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        "book_name, expected_result",
        [
            ['Краткое название', True],
            ['Книга с очень длинным названием, которое превышает сорок один символ', False],
            ['', False],
        ],
    )
    def test_add_new_book_different_names(self, book_name, expected_result):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected_result

    @pytest.mark.parametrize(
        "book_name, genre, expected_genre",
        [
            ['Мастер и Маргарита', 'Фантастика', 'Фантастика'],
            ['Мастер и Маргарита', 'Поэзия', ''],
            ['Неизвестная книга', 'Комедии', None],
        ],
    )
    def test_set_book_genre(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize(
        "book_name, genre, expected_genre",
        [
            ['Мастер и Маргарита', 'Фантастика', 'Фантастика'],
            ['Неизвестная книга', 'Комедии', None],
        ],
    )

    def test_get_book_genre(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize(
        "books, genres, query_genre, expected_books",
        [
            [['Гарри Поттер', 'Оно', 'Вий'], ['Фантастика', 'Ужасы', 'Ужасы'], 'Ужасы', ['Оно', 'Вий']],
            [['Гарри Поттер', 'Оно', 'Вий'], ['Фантастика', 'Ужасы', 'Ужасы'], 'Фантастика', ['Гарри Поттер']],
            [['Гарри Поттер', 'Оно', 'Вий'], ['Фантастика', 'Ужасы', 'Ужасы'], 'Мультфильмы', []],
        ],
    )
    def test_get_books_with_specific_genre(self, books, genres, query_genre, expected_books):
        collector = BooksCollector()
        for i in range(len(books)):
            collector.add_new_book(books[i])
            collector.set_book_genre(books[i], genres[i])
        assert collector.get_books_with_specific_genre(query_genre) == expected_books

    @pytest.mark.parametrize(
        "book_name, genre, expected_books_genre",
        [
            ['Мастер и Маргарита', 'Фантастика', {'Мастер и Маргарита': 'Фантастика'}],
            ['', 'Комедии', {}],
        ],
    )
    def test_get_books_genre(self, book_name, genre, expected_books_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_genre() == expected_books_genre

    @pytest.mark.parametrize(
        "books, genres, expected_books",
        [
            [['Гарри Поттер', 'Молчание ягнят', 'Смешарики'], ['Фантастика', 'Детективы', 'Мультфильмы'], ['Гарри Поттер', 'Смешарики']],
            [['Оно'], ['Ужасы'], []],
        ]
    )
    def test_get_books_for_children(self, books, genres, expected_books):
        collector = BooksCollector()
        for i in range(len(books)):
            collector.add_new_book(books[i])
            collector.set_book_genre(books[i], genres[i])
        assert collector.get_books_for_children() == expected_books

    @pytest.mark.parametrize(
        "book_name, expected_in_favorites, expected_count_in_favorites",
        [
            ['Смешарики', True, 1],
            ['', False, 0],
        ],
    )
    def test_add_book_in_favorites(self, book_name, expected_in_favorites, expected_count_in_favorites):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert (book_name in collector.get_list_of_favorites_books()) == expected_in_favorites
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == expected_count_in_favorites

    @pytest.mark.parametrize(
        "book_name, add_in_favorites, expected_count_in_favorites, expected_result",
        [
            ['Гарри Поттер', True, 1, False],
            ['Гарри Поттер', False, 0, False],
        ],
    )
    def test_delete_book_from_favorites(self, book_name, add_in_favorites, expected_count_in_favorites, expected_result):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        if add_in_favorites:
            collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == expected_count_in_favorites
        collector.delete_book_from_favorites(book_name)
        assert (book_name in collector.get_list_of_favorites_books()) == expected_result

    @pytest.mark.parametrize(
        "book_name, add_in_favorites, expected_favorites_books",
        [
            ['Мастер и Маргарита', True, ['Мастер и Маргарита']],
            ['Кошки-мышки', False, []],
            ['', True, []],
        ],
    )
    def test_get_list_of_favorites_books(self, book_name, add_in_favorites, expected_favorites_books):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        if add_in_favorites:
            collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == expected_favorites_books

