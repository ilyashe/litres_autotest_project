import allure
from allure_commons.types import Severity

from data.users import User
from model.pages.main_page import main_page
from model.pages.profile_page import profile_page
import os


@allure.epic('Авторизация')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка авторизации юзера')
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


@allure.epic('Авторизация')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка авторизации юзера')
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


@allure.epic('Авторизация')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка авторизации юзера')
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