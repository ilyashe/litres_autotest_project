from selene import browser, have
import allure


class ProfilePage:
    @allure.step("Открытие страницы профиля")
    def open(self):
        browser.open("me/profile/")
        return self

    @allure.step("Открытие редактирования профиля")
    def open_profile_edit(self):
        browser.element('[data-testid=profile__userNameMain]').click()
        return self

    @allure.step("Логаут пользователя")
    def logout(self):
        browser.element('[data-testid=profile__logout--button]').click()
        browser.all('[data-testid=button__content]').element_by(have.text('Выйти')).click()
        return self

profile_page = ProfilePage()
