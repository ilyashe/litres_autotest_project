from data.books import Book
from model.pages.mobile_pages.main_page import main_page
from model.pages.mobile_pages.search_result_page import search_result_page
from model.pages.mobile_pages.book_page import book_page
from model.pages.mobile_pages.favorite_page import favorite_page

def test_adding_book_to_favorite(android_management):
    book = Book(
        title='Пустые поезда 2022 года',
        author='Дмитрий Данилов'
    )
    main_page.open()

    # WHEN
    main_page.search_book(book)
    search_result_page.open_book()
    book_page.add_book_to_favorite()
    main_page.open_favorite_page()

    # THEN
    favorite_page.should_find_book_in_favorite(book)
