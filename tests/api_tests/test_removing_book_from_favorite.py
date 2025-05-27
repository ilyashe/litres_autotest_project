import allure
from allure_commons.types import Severity
from data.books import Book
from litres.api_helpers import favorite, get_from_result


pytestmark = [
    allure.label('layer', 'api'),
    allure.suite('API'),
    allure.feature('Избранное'),
    allure.story('Проверка удаления книги из избранного')
]

@allure.title(f'Удаление книги из избранного')
@allure.label('owner', 'Ilya Shebanov')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
def test_removing_book_from_favorite():
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов',
        book_api_id='69581329'
    )

    #WHEN
    put_result = favorite.put_add_book_to_favorite(book)
    session_id = get_from_result.get_session_id_from_api(put_result)
    delete_result = favorite.delete_book_from_favorite(book, session_id)

    #THEN
    favorite.delete_book_from_favorite_should_be_successful(delete_result)
