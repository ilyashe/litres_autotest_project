from selene import browser, have, be, command
import allure


class BookPage:
    def add_book_to_basket(self):
        with allure.step('Добавление книги в корзину'):
            browser.driver.refresh()
            if browser.element('[data-testid=book__addToCartButton]').with_(timeout=7).matching(be.present):
                browser.element('[data-testid=book__addToCartButton]').should(be.clickable).click()
            else:
                browser.element('[data-testid=book-sale-block__PPD--wrapper]').should(be.clickable).click()
                browser.element('[data-testid=book__addToCartButton]').should(be.clickable).click()


            # if browser.element('[data-testid=book__addToCartButton]').with_(timeout=7).matching(be.present):
            #     while not browser.element('[data-testid="book__goToCartButton"]').matching(be.present):
            #         browser.element('[data-testid=book__addToCartButton]').should(be.clickable).click()
            # else:
            #     browser.element('[data-testid=book-sale-block__PPD--wrapper]').should(be.clickable).click()
            #     while not browser.element('[data-testid="book__goToCartButton"]').matching(be.present):
            #         browser.element('[data-testid=book__addToCartButton]').should(be.clickable).click()
            return self

    def should_book_with_price(self, book):
        with allure.step('Проверка цены книги'):
            browser.element('[data-testid=book__saleBlock--discountPrice]').should(have.text(f'{book.price} ₽'))
            return self

book_page = BookPage()
