from selene import browser, have, be, command
import allure


class BookPage:
    def add_book_to_basket(self):
        with allure.step('Добавление книги в корзину'):
            if browser.element('[data-testid=book__addToCartButton]').matching(be.visible):
                browser.element('[data-testid=book__addToCartButton]').perform(command.js.click)
            else:
                browser.element('[data-testid="book-sale-block__PPD--wrapper"]').perform(command.js.click)
                browser.element('[data-testid=book__addToCartButton]').click()
            return self

    def should_book_with_price(self, book):
        with allure.step('Проверка цены книги'):
            browser.element('[data-testid=book__saleBlock--discountPrice]').should(have.text(f'{book.price} ₽'))
            return self

book_page = BookPage()
