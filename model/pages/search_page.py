from selene import browser, have
import allure


class SearchPage:
    def open(self):
        with allure.step("Открытие страницы поиска"):
            browser.open("search/")
            return self

    def should_find_book_with_title(self, book):
        with allure.step("Открытие редактирования профиля"):
            browser.all('[data-testid=art__title]').first.should(have.text(book.title))
            return self

search_page = SearchPage()
