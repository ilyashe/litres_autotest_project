import allure
from allure_commons.types import Severity
from requests import session

from data.books import Book
from model.api_helpers import helpers

@allure.epic('Удаление книги из избранного')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка удаления книги из избранного')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
def test_removing_book_from_favorite():
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов',
        book_api_id='69581329'
    )

    #WHEN
    put_result = helpers.put_add_book_to_favorite(book)
    session_id = helpers.get_session_id_from_api(put_result)
    delete_result = helpers.delete_book_from_favorite(book, session_id)

    #THEN
    helpers.delete_book_from_favorite_should_be_successful(delete_result)
