import allure
from allure_commons.types import Severity
from data.books import Book
from litres.pages.web_pages.main_page import main_page
from litres.pages.web_pages.search_page import search_page
from data.users import User
import os

pytestmark = [
    allure.label('layer', 'web'),
    allure.suite('Web'),
    allure.feature('Поиск книги'),
    allure.story('Проверка поиска книги')
]

@allure.title(f'Поиск книги')
@allure.label('owner', 'Ilya Shebanov')
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

@allure.title(f'Поиск несуществующей книги')
@allure.label('owner', 'Ilya Shebanov')
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

@allure.title(f'Поиск книги под авторизованным юзером')
@allure.label('owner', 'Ilya Shebanov')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
def test_search_book_by_auth_user():
    user = User(
        first_name='Andrey',
        last_name='Sokolov',
        email=os.getenv('EMAIL'),
        password=os.getenv('PASSWORD')
    )
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов'
    )
    main_page.open_by_auth_user(user)

    #WHEN
    main_page.search_book(book)

    #THEN
    search_page.should_find_book_with_title(book)
