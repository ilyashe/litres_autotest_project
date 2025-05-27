from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class ProfilePage:
    def change_language_to_russian(self):
        with step('Изменение языка интерфейса на русский'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')).click()
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Русский")')).click()
            browser.element((AppiumBy.ID, 'android:id/button1')).click()
            browser.element(
                (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_and_dont_ask_again_button')
                ).click()
            return self

    def should_language_be_russian(self):
        with step('Проверка, что язык интерфейса русский'):
            browser.element((AppiumBy.ID, 'ru.litres.android:id/login_button')
                            ).should(have.text('ВОЙТИ/ЗАРЕГИСТРИРОВАТЬСЯ'))
            return self

profile_page = ProfilePage()
