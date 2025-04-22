from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have



def test_search_book(android_management):

    with ((step('Прокрутить список языков до RUSSIAN'))):
        browser.element((AppiumBy.ID, 'ru.litres.android:id/choosebutton')).should(be.visible)
        browser.driver.swipe(550, 1350, 550, 1250)
        browser.element((AppiumBy.ID, 'ru.litres.android:id/choosebutton')).click()
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')).click()
        browser.element((AppiumBy.ID, 'ru.litres.android:id/circleButtonSubscriptionPaywallClose')).click()
        browser.element((AppiumBy.ID, 'ru.litres.android:id/search')).click()
        browser.element((AppiumBy.ID, 'ru.litres.android:id/et_search_query')
                        ).type('Дмитрий Данилов Пустые поезда 2022 года')
        browser.element((AppiumBy.ID, 'ru.litres.android:id/textViewItemSearchSuggestText')).click()
        browser.element((AppiumBy.XPATH,
                         '(//android.widget.TextView[@resource-id="ru.litres.android:id/textViewBookName"])[1]')
                        ).should(have.text('Пустые поезда 2022 года'))
