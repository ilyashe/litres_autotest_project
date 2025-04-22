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

def get_bsk_cookie_from_api(result):
    with step('Получение BSK cookie'):
        bsk_cookie = result.cookies.get('BSK')
        return bsk_cookie

def put_add_book_to_favorite(book):
    with step('Добавление книги в избранное'):
        result = litres_api_request(
            path=f'wishlist/arts/{book.book_api_id}',
            method='PUT'
        )
        return result

def put_add_book_to_favorite_should_be_successful(result):
    with step('Проверка, что книга добавлена в избранное успешно'):
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
    with step('Проверка, что книга удалена из избранного успешно'):
        assert result.status_code == 204

def put_add_book_to_basket(book):
    with step('Добавление книги в корзину'):
        result = litres_api_request(
            path='cart/arts/add',
            method='PUT',
            data=json.dumps({
                "art_ids":[book.book_api_id]
            })
        )
        return result

def put_add_book_to_basket_should_be_successful(result, book):
    with step('Проверка, что книга добавлена в корзину успешно'):
        assert result.status_code == 200
        validate(result.json(), schema=schemas.put_add_book_to_basket_successful)
        assert result.json()['payload']['data']['added_art_ids'][0] == int(book.book_api_id)

def put_add_book_with_nonexistent_id_to_basket_should_be_without_book(result):
    with step('Проверка, что книга не добавлена в корзину'):
        assert result.status_code == 200
        validate(result.json(), schema=schemas.put_add_book_to_basket_successful)
        assert result.json()['payload']['data']['added_art_ids'] == []

def put_add_book_with_too_long_id_to_basket_should_be_error(result):
    with (step('Проверка, что возвращается ошибка валидации')):
        assert result.status_code == 422
        validate(result.json(), schema=schemas.put_add_book_to_basket_validation_error)
        assert result.json()['error']['error_descriptions'][0]['msg'] == ('Input should be less than or equal to '
                                                                          '4294967295')

def put_remove_book_from_basket(book, bsk_cookie=''):
    with step('Удаление книги из корзины'):
        result = litres_api_request(
            path='cart/arts/remove',
            method='PUT',
            data=json.dumps({
                "art_ids":[book.book_api_id]
            }),
            headers={
                'cookie': f'BSK={bsk_cookie}'
            }
        )
        return result

def put_remove_book_from_basket_should_be_successful(result):
    with step('Проверка, что книга удалена из корзины успешно'):
        assert result.status_code == 204
        assert result.cookies.get('BSK') is None

def get_basket_status(bsk_cookie=''):
    with step('Получения статуса корзины'):
        result = litres_api_request(
            path='cart/status',
            method='GET',
            headers={
                'cookie': f'BSK={bsk_cookie}'
            }
        )
        return result

def get_basket_status_basket_should_be_empty(result):
    with step('Проверка, что корзина пустая'):
        assert result.status_code == 200
        validate(result.json(), schema=schemas.get_basket_status)
        assert result.json()['payload']['data']['arts_in_cart'] == []

def get_basket_status_basket_should_be_with_book(result, book):
    with step('Проверка, что в корзине есть книга'):
        assert result.status_code == 200
        validate(result.json(), schema=schemas.get_basket_status)
        assert result.json()['payload']['data']['arts_in_cart'][0] == int(book.book_api_id)