import allure
from allure_commons.types import Severity
from data.books import Book
from model.pages.web_pages.main_page import main_page
from model.pages.web_pages.search_page import search_page
from model.pages.web_pages.book_page import book_page
from model.pages.web_pages.basket_page import basket_page
from utils import tools


pytestmark = [
    allure.label('layer', 'web'),
    allure.suite('Web'),
    allure.feature('Корзина'),
    allure.story('Проверка удаления книги из корзины')
]

@allure.title(f'Удаление книги из корзины')
@allure.label('owner', 'Ilya Shebanov')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
def test_removing_book_from_basket():
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов',
        price=419
    )
    main_page.open()

    #WHEN
    main_page.search_book(book)
    search_page.open_book()
    tools.open_new_window(window_number=1)
    book_page.add_book_to_basket()
    main_page.close_modal()
    main_page.open_basket()
    basket_page.remove_book_from_basket()

    # THEN
    basket_page.basket_should_be_empty()
