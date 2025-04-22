import allure
from allure_commons.types import Severity
from data.books import Book
from model.api_helpers import helpers

@allure.epic('Добавление книги в корзину')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка добавления книги в корзину')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
def test_adding_book_to_basket():
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов',
        book_api_id='69581329'
    )

    #WHEN
    result = helpers.put_add_book_to_basket(book)

    #THEN
    helpers.put_add_book_to_basket_should_be_successful(result, book)

@allure.epic('Добавление книги в корзину')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка добавления книги в корзину')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
def test_adding_book_with_nonexistent_id_to_basket():
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов',
        book_api_id='4294967295'
    )

    #WHEN
    result = helpers.put_add_book_to_basket(book)

    #THEN
    helpers.put_add_book_with_nonexistent_id_to_basket_should_be_without_book(result)

@allure.epic('Добавление книги в корзину')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка добавления книги в корзину')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
def test_adding_book_with_too_long_id_to_basket():
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов',
        book_api_id='4294967296'
    )

    #WHEN
    result = helpers.put_add_book_to_basket(book)

    #THEN
    helpers.put_add_book_with_too_long_id_to_basket_should_be_error(result)
