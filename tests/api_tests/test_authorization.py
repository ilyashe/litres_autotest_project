import allure
from allure_commons.types import Severity

from data.users import User
import os
from model.api_helpers import auth

@allure.epic('Авторизация')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка авторизации юзера')
@allure.tag('api')
@allure.severity(Severity.CRITICAL)
def test_authorization_registered_user():
    user = User(
        first_name='Andrey',
        last_name='Sokolov',
        email=os.getenv('EMAIL'),
        password=os.getenv('PASSWORD')
    )

    #WHEN
    result = auth.post_auth(user)

    #THEN
    auth.post_auth_user_should_be_authorized(result)

@allure.epic('Авторизация')
@allure.label('owner', 'Ilya Shebanov')
@allure.feature('Проверка авторизации юзера')
@allure.tag('api')
@allure.severity(Severity.CRITICAL)
def test_authorization_unregistered_user():
    user = User(
        first_name='Andrey',
        last_name='Sokolov',
        email=os.getenv('UNREGISTERED_EMAIL'),
        password=os.getenv('PASSWORD')
    )

    #WHEN
    result = auth.post_auth(user)

    #THEN
    auth.post_auth_user_should_not_be_authorized(result)
