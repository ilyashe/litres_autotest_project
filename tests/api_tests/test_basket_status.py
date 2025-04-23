import allure
from allure_commons.types import Severity
from data.books import Book
from model.api_helpers import basket, get_from_result


@allure.epic('Статус корзины')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка статуса корзины')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
def test_empty_basket_status():
    #WHEN
    result = basket.get_basket_status()

    #THEN
    basket.get_basket_status_basket_should_be_empty(result)

@allure.epic('Статус корзины')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка статуса корзины')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
def test_basket_with_book_status():
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов',
        book_api_id='69581329'
    )

    #WHEN
    put_result = basket.put_add_book_to_basket(book)
    bsk_cookie = get_from_result.get_bsk_cookie_from_api(put_result)
    status_result = basket.get_basket_status(bsk_cookie)

    #THEN
    basket.get_basket_status_basket_should_be_with_book(status_result, book)
