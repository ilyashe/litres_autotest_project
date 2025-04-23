from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class BookPage:
    def add_book_to_favorite(self):
        with step('Добавление книги в избранное'):
            browser.element((AppiumBy.ID,'ru.litres.android:id/imageViewBookCardFavourite')).click()
            return self

    def should_find_book_with_title(self, book):
        with step('Проверка, что книга нашлась'):
            browser.element((AppiumBy.XPATH,
                             '(//android.widget.TextView[@resource-id="ru.litres.android:id/textViewBookName"])[1]')
                            ).should(have.text(book.title))
            return self

book_page = BookPage()
