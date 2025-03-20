import time

from selene import browser, have, command
import allure


class MainPage:
    def open(self):
        with allure.step('Открытие главной страницы'):
            browser.open('')
            return self

    def fill_email(self, user):
        with allure.step('Ввод имейла'):
            browser.element('[data-testid=tab-login]').click()
            browser.element('[data-testid=auth__input--enterEmailOrLogin]').type(user.email)
            browser.element('[data-testid=auth__button--continue]').click()
            return self

    def fill_password(self, user):
        with allure.step('Ввод пароля'):
            browser.element('[data-testid=auth__input--enterPassword]').type(user.password)
            browser.element('[data-testid=auth__button--enter]').click()
            return self

    def open_profile(self):
        with allure.step('Открытие страницы профиля'):
            browser.element('[data-testid=header__profile-button]').perform(command.js.click)
            return self

    def open_basket(self):
        with allure.step('Открытие страницы корзины'):
            browser.element('[data-testid=tab-basket]').click()
            return self

    def search_book(self, book):
        with allure.step('Поиск книги'):
            browser.element('[data-testid=search__input]').type(f'{book.author} {book.title}')
            browser.element('[data-testid=search__button]').perform(command.js.click)
            return self

    def close_modal(self):
        with allure.step('Закрытие модального окна'):
            browser.all('#modal').with_(timeout=5).wait_until(
                have.size_greater_than_or_equal(1)
            )
            browser.all('#modal').perform(command.js.remove)
            return self

    def user_should_be_authorized(self, user):
        with allure.step('Проверка, что юзер авторизован'):
            browser.element('[name=first_name]').should(have.value(user.first_name))
            browser.element('[name=last_name]').should(have.value(user.last_name))
            return self

    def user_should_not_be_authorized(self):
        with allure.step('Проверка, что юзер не авторизован'):
            (browser.element('[data-testid=textbox--input__error]').
             should(have.exact_text('Неверное сочетание логина и пароля')))
            return self

    def user_can_be_registered(self):
        with allure.step('Проверка, что юзер может быть зарегистрирован'):
            browser.element('[data-testid=authorization-popup]').should(have.text('Адрес свободен для регистрации'))
            return self

    def user_should_be_unauthorized(self):
        with allure.step('Проверка, что юзер разлогинен'):
            browser.element('[data-testid=tab-login]').should(have.text('Войти'))
            return self

main_page = MainPage()
