from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have


class MainPage:
    def open(self):
        with step('Открытие главной страницы'):
            browser.element((AppiumBy.ID, 'ru.litres.android:id/choosebutton')).should(be.visible)
            browser.driver.swipe(550, 1350, 550, 1250)
            browser.element((AppiumBy.ID, 'ru.litres.android:id/choosebutton')).click()
            browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')).click()
            elements = browser.all((AppiumBy.ID, 'ru.litres.android:id/circleButtonSubscriptionPaywallClose'))
            if elements.with_(timeout=4).wait_until(have.size_greater_than(0)):
                elements.first.should(be.clickable).click()
            return self

    def open_favorite_page(self):
        with step('Открытие избранного'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'My books')).click()
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Favorites")')).click()
            return self

    def open_profile_page(self):
        with step('Открытие профиля'):
            browser.element((AppiumBy.ID, 'ru.litres.android:id/ll_profile_menu_item')).click()
            return self

    def search_book(self, book):
        with step('Поиск книги'):
            browser.element((AppiumBy.ID, 'ru.litres.android:id/search')).click()
            browser.element((AppiumBy.ID, 'ru.litres.android:id/et_search_query')).type(f'{book.author} {book.title}')
            browser.element((AppiumBy.ID, 'ru.litres.android:id/textViewItemSearchSuggestText')).click()
            return self


main_page = MainPage()