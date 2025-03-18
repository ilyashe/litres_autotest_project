from selene import browser, have
import allure


class ProfilePage:
    def open(self):
        with allure.step('Открытие страницы профиля'):
            browser.open('me/profile/')
            return self

    def open_profile_edit(self):
        with allure.step('Открытие редактирования профиля'):
            browser.element('[data-testid=profile__userNameMain]').click()
            return self

    def logout(self):
        with allure.step('Логаут пользователя'):
            browser.element('[data-testid=profile__logout--button]').click()
            browser.all('[data-testid=button__content]').element_by(have.text('Выйти')).click()
            return self

profile_page = ProfilePage()
