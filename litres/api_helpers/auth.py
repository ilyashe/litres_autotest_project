import json
from allure_commons._allure import step
from jsonschema import validate
from litres.schemas import schemas
from utils.api_request_with_attach import litres_api_request


def post_auth(user):
    with step('Авторизация юзера'):
        result = litres_api_request(
            path='auth/login',
            data=json.dumps({
            "login": user.email,
            "password": user.password
        }),
            headers={
                'app-id': '115'
            }
        )
        return result


def post_auth_user_should_be_authorized(result):
    with step('Проверка, что юзер авторизован'):
        assert result.status_code == 200
        validate(result.json(), schema=schemas.post_auth_successful)


def post_auth_user_should_not_be_authorized(result):
    with step('Проверка, что юзер не авторизован'):
        assert result.status_code == 401
        validate(result.json(), schema=schemas.post_auth_unsuccessful)
        assert result.json()['error']['type'] == 'Unauthorized'
        assert result.json()['error']['title'] == 'Incorrect user data'
