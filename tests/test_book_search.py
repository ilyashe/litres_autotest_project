import allure
from allure_commons.types import Severity

from data.books import Book
from model.pages.main_page import main_page
from model.pages.search_page import search_page


@allure.epic('Поиск книги')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка поиска книги')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
def test_search_book():
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов'
    )
    main_page.open()

    #WHEN
    main_page.search_book(book)

    #THEN
    search_page.should_find_book_with_title(book)

@allure.epic('Поиск книги')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка поиска книги')
@allure.tag('web')
@allure.severity(Severity.MINOR)
def test_search_non_existent_book():
    book = Book(
        title='кпещлпзекорьещетн',
        author='епекипкбищзеьищнет'
    )
    main_page.open()

    #WHEN
    main_page.search_book(book)

    #THEN
    search_page.should_find_empty_result()