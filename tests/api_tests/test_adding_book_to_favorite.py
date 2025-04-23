import allure
from allure_commons.types import Severity
from data.books import Book
from model.api_helpers import favorite


pytestmark = [
    allure.label("layer", 'api')
]

@allure.epic('Добавление книги в избранное')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка добавления книги в избранное')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
def test_adding_book_to_favorite():
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов',
        book_api_id='69581329'
    )

    #WHEN
    result = favorite.put_add_book_to_favorite(book)

    #THEN
    favorite.put_add_book_to_favorite_should_be_successful(result)
