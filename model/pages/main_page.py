from selene import browser, have
import allure


class MainPage:
    @allure.step("Открытие главной страницы")
    def open(self):
        browser.open("")
        return self

    @allure.step("Ввод имейла")
    def fill_email(self, user):
        browser.element('[data-testid=tab-login]').click()
        browser.element('[data-testid=auth__input--enterEmailOrLogin]').type(user.email)
        browser.element('[data-testid=auth__button--continue]').click()
        return self

    @allure.step("Ввод пароля")
    def fill_password(self, user):
        browser.element('[data-testid=auth__input--enterPassword]').type(user.password)
        browser.element('[data-testid=auth__button--enter]').click()
        return self

    @allure.step("Открытие страницы профиля")
    def open_profile(self):
        browser.element('[data-testid=user-button]').click()
        return self

    @allure.step("Проверка, что юзер авторизован")
    def user_should_be_authorized(self, user):
        browser.element('[name=first_name]').should(have.value(user.first_name))
        browser.element('[name=last_name]').should(have.value(user.last_name))
        return self

    @allure.step("Проверка, что юзер не авторизован")
    def user_should_not_be_authorized(self):
        (browser.element('[data-testid=textbox--input__error]').
         should(have.exact_text('Неверное сочетание логина и пароля')))
        return self

    @allure.step("Проверка, что юзер может быть зарегистрирован")
    def user_can_be_registered(self):
        browser.element('[data-testid=authorization-popup]').should(have.text('Адрес свободен для регистрации'))
        return self

    @allure.step("Проверка, что юзер разлогинен")
    def user_should_be_unauthorized(self):
        browser.element('[data-testid=tab-login]').should(have.text('Войти'))
        return self

main_page = MainPage()
