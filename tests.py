from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

#Провряем переменные в __init__
    #Проверяем, что books_genre это пустой словарь
    def test_init_books_genre_true(self):
        books_init_collection = BooksCollector()
        assert books_init_collection.books_genre == {}

    #Проверяем, что favorites это пустой список
    def test_init_favorites_true(self):
        books_init_favorite = BooksCollector()
        assert books_init_favorite.favorites == []

    #Проверяем, что genre содержит правильный список жанров
    def test_init_genre_true(self):
        book_init_genre = BooksCollector()
        assert book_init_genre.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы',
                             'Комедии']

    #Проверяем, что genre_age_rating содержит правильный список жанров
    def test_init_genre_age_rating_true(self):
        books_init_age_rating = BooksCollector()
        assert books_init_age_rating.genre_age_rating == ['Ужасы',
                                        'Детективы']

#Проверяем метод add_new_book
    #Проверяем, что новая книга добавилась
    def test_add_new_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('НеДжедайские техники')
        assert 'НеДжедайские техники' in collector.books_genre

    #Проверяем, что пустая книга не добавилась
    def test_add_new_book_name_empty_name_true(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.books_genre

    #Провряем, что книга с длинным названием не добавилась
    def test_add_new_book_name_long_name_true(self):
        collector = BooksCollector()
        collector.add_new_book('аааааааааааааааааааааааааааааааааааааааааааааааааа')
        assert 'аааааааааааааааааааааааааааааааааааааааааааааааааа' not in collector.books_genre

#Проверяем метод set_book_genre
    #Проверяем, что жанр добавился к книге
    def test_set_book_genre_add_new_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('НеДжедайские техники')
        collector.set_book_genre('НеДжедайские техники', 'Ужасы')
        assert collector.books_genre['НеДжедайские техники'] == 'Ужасы'

    #Проверяем, что неизвестный жанр не добавился к книге
    def test_set_book_genre_add_invalid_genre_genres_not_changed(self):
        collector = BooksCollector()
        collector.add_new_book('НеДжедайские техники')
        collector.set_book_genre('НеДжедайские техники', 'Такого жанра нет')
        #assert 'Такого жанра нет' not in collector.set_book_genre['НеДжедайские техники'] - Здесь, видимо, ошибка была, что я обращаюсь в assert к set_book_genre, а за вывод ведь отвечает get_book_genre
        #Отславляю эту строчку лишь для того, чтобы если я что-то сделал не так, то меня поправили бы
        assert collector.get_book_genre('НеДжедайские техники') == ''

    #Проверяем, что пустой жанр не добавился к книге
    def test_set_book_genre_add_empty_genre_genres_not_changed(self):
        collector = BooksCollector()
        collector.add_new_book('НеДжедайские техники')
        collector.set_book_genre('НеДжедайские техники', '')
        assert collector.get_book_genre('НеДжедайские техники') == '' #Здесь была такая же ошибка. Если можно как-то по-другому проверить, то я буду счастлив, если намекнете. Просто я всегда думал, что методы должны как-то изолированны друг от друга проверяться

#Проверяем метод get_book_genre
    def test_get_book_genre_existing_book_with_genre_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('НеДжедайские техники')
        collector.set_book_genre('НеДжедайские техники', 'Ужасы')
        assert collector.get_book_genre('НеДжедайские техники') == 'Ужасы'  # Ожидается True

    def test_get_book_genre_existing_book_no_genre_get_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('НеДжедайские техники')
        assert collector.get_book_genre('НеДжедайские техники') == ''  # Ожидается True

#Проверяем метод get_books_with_specific_genre
    #Метод показался мне что-то прям слишком сложным :(((
    #Потратил всё время, которое у меня было, на решение технических проблем с терминалом Cygwin и связью PyCharm <-> Pytest
    #Ввиду чего написал всего один тест, но и по заданию проекта достаточно всего 1 теста на метод :((( Извините :((((

    #Проверяет, что метод возвращает пустой список, если книги по данному жанру нет в коллекции
    def test_get_books_with_specific_genre_no_books_show_empty_list(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre('Ужасы') == []
#Провреяем метод get_books_genre
    #Здесь тоже решил пока что не заморачиваться, ввиду малого времени :((

    #Проверяет, что метод возвращает пустой словарь, если в словарь не добавлена ни одна книга
    def test_get_books_genre_empty_dict(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

#Проверяем метод get_books_for_children
    # Здесь тоже всего один тест пока что :(((
    # Постараюсь попозже добавить хоть что-нибудь ещё. Если не добавил, то не успел

    #Проверяет, что метод возвращает пустой список, если книг вообще нет
    def test_get_books_for_children_no_books_empty_list(self):
        collector = BooksCollector()
        assert collector.get_books_for_children() == []

#Проверяем метод add_book_in_favorites
    #Проверяет, что метод не добавляет несуществующую книгу в избранное
    def test_add_book_in_favorites_unknown_book_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('НеДжедайские техники')
        assert 'НеДжедайские техники' not in collector.favorites

    #Проверяет, что метод добавляет книгу в избранное
    def test_add_book_in_favorites_add_book_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('НеДжедайские техники')
        collector.add_book_in_favorites('НеДжедайские техники')
        assert 'НеДжедайские техники' in collector.favorites

    #Проверяем, что метод не добавляет книгу повторно
    def test_add_book_in_favorites_add_book_that_already_exist_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book('НеДжедайские техники')
        collector.add_new_book('Тестирование Дот NET')
        collector.add_book_in_favorites('НеДжедайские техники')
        collector.add_book_in_favorites('Тестирование Дот NET')
        collector.add_book_in_favorites('НеДжедайские техники')
        assert len(collector.favorites) == 2

#Проверяем метод delete_book_from_favorites
    #Проверяем, что метод удаляет книгу из избранного
    def test_delete_book_from_favorites_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('НеДжедайские техники')
        collector.add_book_in_favorites('НеДжедайские техники')
        collector.delete_book_from_favorites('НеДжедайские техники')
        assert 'НеДжедайские техники' not in collector.favorites

    #Проверяем, что при удалении книги, которой не было в избранном, ничего не изменилось
    def test_delete_book_from_favorites_delete_book_that_doesnt_exist_nothing_has_changed(self):
        collector = BooksCollector()
        collector.add_new_book('НеДжедайские техники')
        #past_condition = list(collector.favorites)
        #future_condition = collector.delete_book_from_favorites('НеДжедайские техники')
        #assert past_condition == future_condition
        collector.delete_book_from_favorites('НеДжедайские техники')
        assert 'НеДжедайские техники' not in collector.favorites

#Проверяем метод get_list_of_favorites_books
    #Провряем, что список возвращаем пустой список, если в нем нет ни одной книги
    def test_get_list_of_favorites_books_no_books_list_is_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    #Проверяем, что метод выводит список, если там есть хотя бы одна, добавленная в избранное, книга
    def test_get_list_of_favorites_books_one_book_list_with_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('НеДжедайские техники')
        collector.add_book_in_favorites('НеДжедайские техники')
        assert collector.get_list_of_favorites_books() == ['НеДжедайские техники']

