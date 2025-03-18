from selene import browser, have
import allure


class SearchPage:
    def open(self):
        with allure.step('Открытие страницы поиска'):
            browser.open('search/')
            return self

    def should_find_book_with_title(self, book):
        with allure.step('Проверка, что книга нашлась'):
            browser.all('[data-testid=art__title]').first.should(have.text(book.title))
            return self

    def should_find_empty_result(self, book):
        with allure.step('Проверка, что нет результатов'):
            browser.element('[data-testid=search-title__wrapper]').should(have.text('ничего не найдено'))
            return self

search_page = SearchPage()
