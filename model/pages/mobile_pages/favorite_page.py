from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class FavoritePage:
    def should_find_book_in_favorite(self, book):
        with step('Проверка, что книга есть в избранном'):
            browser.element((AppiumBy.ID, 'ru.litres.android:id/textViewBookName')
                            ).should(have.text(book.title))
            return self

favorite_page = FavoritePage()