import allure
from allure_commons.types import Severity
from data.books import Book
from model.api_helpers import basket, get_from_result


pytestmark = [
    allure.label('layer', 'api'),
    allure.parent_suite('API'),
    allure.suite('Корзина'),
    allure.feature('Проверка удаления книги из корзины')
]

@allure.title(f'Удаление книги из корзины')
@allure.label('owner', 'Ilya Shebanov')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
def test_removing_book_from_basket():
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов',
        book_api_id='69581329'
    )

    #WHEN
    put_result = basket.put_add_book_to_basket(book)
    bsk_cookie = get_from_result.get_bsk_cookie_from_api(put_result)
    delete_result = basket.put_remove_book_from_basket(book, bsk_cookie)
    #THEN
    basket.put_remove_book_from_basket_should_be_successful(delete_result)
