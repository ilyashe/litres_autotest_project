from selene import browser, have
import allure


class BasketPage:
    def remove_book_from_basket(self):
        with allure.step('Удаление книги из корзины'):
            browser.all('[data-testid=cart__listDeleteButton]').first.click()
            browser.all('[data-testid=button__content]').element_by(have.text('Удалить')).click()
            return self

    def book_should_be_added_to_basket(self, book):
        with allure.step('Проверка наличия книги в корзине'):
            browser.element('[data-testid=cart__bookCardTitle--wrapper]').should(have.text(book.title))
            browser.element('[data-testid=cart__bookCardAuthor--wrapper]').should(have.text(book.author))
            browser.element('[data-testid=cart__bookCardDiscount--wrapper]').should(have.text(str(book.price)))
            return self

    def basket_should_be_empty(self):
        with allure.step('Проверка, что корзина пустая'):
            browser.element('[data-testid=cart__emptyState--wrapper]').should(have.text('Корзина пуста'))
            return self

basket_page = BasketPage()
