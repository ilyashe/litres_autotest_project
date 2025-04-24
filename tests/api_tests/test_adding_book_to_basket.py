import allure
from allure_commons.types import Severity
from data.books import Book
from model.api_helpers import basket


pytestmark = [
    allure.label('layer', 'api'),
    allure.suite('API'),
    allure.feature('Корзина'),
    allure.story('Проверка добавления книги в корзину')
]

@allure.title(f'Добавление книги в корзину')
@allure.label('owner', 'Ilya Shebanov')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
def test_adding_book_to_basket():
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов',
        book_api_id='69581329'
    )

    #WHEN
    result = basket.put_add_book_to_basket(book)

    #THEN
    basket.put_add_book_to_basket_should_be_successful(result, book)

@allure.title(f'Добавление книги с несуществующим ID в корзину')
@allure.label('owner', 'Ilya Shebanov')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
def test_adding_book_with_nonexistent_id_to_basket():
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов',
        book_api_id='4294967295'
    )

    #WHEN
    result = basket.put_add_book_to_basket(book)

    #THEN
    basket.put_add_book_with_nonexistent_id_to_basket_should_be_without_book(result)

@allure.title(f'Добавление книги с ID больше лимита в корзину')
@allure.label('owner', 'Ilya Shebanov')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
def test_adding_book_with_too_big_id_to_basket():
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов',
        book_api_id='4294967296'
    )

    #WHEN
    result = basket.put_add_book_to_basket(book)

    #THEN
    basket.put_add_book_with_too_long_id_to_basket_should_be_error(result)
