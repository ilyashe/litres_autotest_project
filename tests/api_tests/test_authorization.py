import allure
from allure_commons.types import Severity
from data.users import User
import os
from litres.api import auth


pytestmark = [
    allure.label('layer', 'api'),
    allure.suite('API'),
    allure.feature('Авторизация'),
    allure.story('Проверка авторизации юзера')
]

@allure.title(f'Авторизация зарегистрированного пользователя')
@allure.label('owner', 'Ilya Shebanov')
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

@allure.title(f'Авторизация незарегистрированного пользователя')
@allure.label('owner', 'Ilya Shebanov')
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
