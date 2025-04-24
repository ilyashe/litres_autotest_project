import allure
from allure_commons.types import Severity
from data.users import User
from model.pages.web_pages.main_page import main_page
from model.pages.web_pages.profile_page import profile_page
import os


pytestmark = [
    allure.label('layer', 'web'),
    allure.suite('Web'),
    allure.feature('Авторизация'),
    allure.story('Проверка логаута юзера')
]

@allure.title(f'Логаут юзера')
@allure.label('owner', 'Ilya Shebanov')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
def test_logout():
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
    profile_page.logout()

    #THEN
    main_page.user_should_be_unauthorized()

@allure.title(f'Логаут юзера с авторизацией через API')
@allure.label('owner', 'Ilya Shebanov')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
def test_logout_with_api_auth():
    user = User(
        first_name='Andrey',
        last_name='Sokolov',
        email=os.getenv('EMAIL'),
        password=os.getenv('PASSWORD')
    )

    main_page.open_by_auth_user(user)
    main_page.open_profile()
    profile_page.logout()

    #THEN
    main_page.user_should_be_unauthorized()
