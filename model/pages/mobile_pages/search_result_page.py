from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class SearchResultPage:
    def open_book(self):
        with step('Открытие страницы книги нажатием на название'):
            browser.element((AppiumBy.XPATH,
                             '(//android.widget.TextView[@resource-id="ru.litres.android:id/textViewBookName"])[1]')
                            ).click()
            return self

    def should_find_book_with_title(self, book):
        with step('Проверка, что книга нашлась'):
            browser.element((AppiumBy.XPATH,
                             '(//android.widget.TextView[@resource-id="ru.litres.android:id/textViewBookName"])[1]')
                            ).should(have.text(book.title))
            return self

search_result_page = SearchResultPage()