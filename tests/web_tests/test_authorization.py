import allure
from allure_commons.types import Severity
from data.users import User
from litres.pages.web_pages.main_page import main_page
from litres.pages.web_pages.profile_page import profile_page
import os


pytestmark = [
    allure.label('layer', 'web'),
    allure.suite('Web'),
    allure.feature('Авторизация'),
    allure.story('Проверка авторизации юзера')
]

@allure.title('Авторизация зарегистрированного пользователя')
@allure.label('owner', 'Ilya Shebanov')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
def test_authorization_registered_user():
    user = User(
        first_name='Andrey',
        last_name='Sokolov',
        email=os.getenv('EMAIL'),
        password=os.getenv('PASSWORD')
    )
    main_page.open()

    #WHEN
    main_page.fill_email(user)
    main_page.fill_password(user)
    main_page.open_profile()
    main_page.close_modal()
    profile_page.open_profile_edit()

    #THEN
    main_page.user_should_be_authorized(user)


@allure.title('Авторизация незарегистрированного пользователя')
@allure.label('owner', 'Ilya Shebanov')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
def test_authorization_unregistered_user():
    user = User(
        first_name='Andrey',
        last_name='Sokolov',
        email=os.getenv('UNREGISTERED_EMAIL'),
        password=os.getenv('PASSWORD')
    )
    main_page.open()

    #WHEN
    main_page.fill_email(user)

    #THEN
    main_page.user_can_be_registered()


@allure.title('Авторизация зарегистрированного пользователя с неверным паролем')
@allure.label('owner', 'Ilya Shebanov')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
def test_authorization_registered_user_with_wrong_password():
    user = User(
        first_name='Andrey',
        last_name='Sokolov',
        email=os.getenv('EMAIL'),
        password=os.getenv('WRONG_PASSWORD')
    )
    main_page.open()

    #WHEN
    main_page.fill_email(user)
    main_page.fill_password(user)

    #THEN
    main_page.user_should_not_be_authorized()
