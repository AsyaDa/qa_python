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

    #проверяем корректность присвоения нового рейтинга книге
    def test_set_book_rating_add_book_and_set_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_rating('Преступление и наказание', 9)
        assert collector.books_rating.get('Преступление и наказание') == 9

    #проверяем, что метод возвращает рейтинг указанной книги
    def test_get_book_rating_add_book_and_get_default_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        assert collector.get_book_rating('Преступление и наказание') == 1


    import pytest

    #проверяем, что книге невозможно поставить некорректный рейтинг
    @pytest.mark.parametrize('new_rating', [-2, 11])
    def test_set_book_rating_add_book_and_set_rating_more_than_10(self, new_rating):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_rating('Преступление и наказание', new_rating)
        assert collector.books_rating.get('Преступление и наказание') == 1

    #проверяем, что метод вернул список книг с заданным рейтингом
    def test_get_books_with_specific_rating_get_books_with_rating_7(self, added_books):
        added_books.set_book_rating('Гордость и предубеждение и зомби', 9)
        added_books.set_book_rating('Что делать, если ваш кот хочет вас убить', 7)
        assert added_books.get_books_with_specific_rating(7) == ['Что делать, если ваш кот хочет вас убить']

    #проверяем, что метод вернул словарь из книг с рейтингами
    def test_get_books_rating_add_two_books_and_get_ratings(self, added_books):
        assert added_books.get_books_rating() == {'Гордость и предубеждение и зомби': 1,
                                                'Что делать, если ваш кот хочет вас убить': 1}

    #проверяем, что одна из добавленных книг добавилась в Избранное
    def test_add_book_in_favorites_one_book_added_to_favorites(self, added_books):
        added_books.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert added_books.favorites == ['Что делать, если ваш кот хочет вас убить']

    #проверяем, что в Избранное не добавится книга, если ее нет в основном списке
    def test_add_book_in_favorites_add_to_favorite_missing_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.favorites == []

    # проверяем, что одна из двух книг в Избранном удалилась
    def test_delete_book_from_favorites_one_of_two_books_deleted_from_favorites(self, added_books):
        added_books.add_book_in_favorites('Гордость и предубеждение и зомби')
        added_books.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        added_books.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert added_books.favorites == ['Гордость и предубеждение и зомби']

    #проверяем, что метод возвращает полный список книг из Избранного
    def test_get_list_of_favorites_books_get_two_books_from_favorites(self, added_books):
        added_books.add_book_in_favorites('Гордость и предубеждение и зомби')
        added_books.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        correct_list_of_fav = ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']
        assert added_books.favorites == correct_list_of_fav
