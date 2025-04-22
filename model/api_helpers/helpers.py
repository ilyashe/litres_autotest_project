from utils.api_request_with_attach import litres_api_request
import json
from jsonschema import validate
from model.schemas import schemas
from allure_commons._allure import step

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

def get_session_id_from_api(result):
    with step('Получение session_id'):
        session_id = result.headers.get('request-session-id')
        return session_id

def put_add_book_to_favorite(book):
    with step('Добавление книги в избранное'):
        result = litres_api_request(
            path=f'wishlist/arts/{book.book_api_id}',
            method='PUT'
        )
        return result

def put_add_book_to_favorite_should_be_successful(result):
    with step('Проверка, что книга добавлена успешно'):
        assert result.status_code == 204

def delete_book_from_favorite(book, session_id):
    with step('Удаление книги из избранного'):
        result = litres_api_request(
            path=f'wishlist/arts/{book.book_api_id}',
            method='DELETE',
            headers={
                'session-id': session_id
            }
        )
        return result

def delete_book_from_favorite_should_be_successful(result):
    with step('Проверка, что книга удалена успешно'):
        assert result.status_code == 204