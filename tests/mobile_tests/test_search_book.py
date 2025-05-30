import allure
from allure_commons.types import Severity
from data.books import Book
from litres.ui.mobile_pages.main_page import main_page
from litres.ui.mobile_pages.search_result_page import search_result_page


pytestmark = [
    allure.label('layer', 'mobile'),
    allure.suite('Mobile'),
    allure.feature('Поиск книги'),
    allure.story('Проверка поиска книги')
]

@allure.title('Поиск книги (Mobile)')
@allure.label('owner', 'Ilya Shebanov')
@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
def test_search_book(android_management):
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов'
    )
    main_page.open()

    # WHEN
    main_page.search_book(book)

    # THEN
    search_result_page.should_find_book_with_title(book)
