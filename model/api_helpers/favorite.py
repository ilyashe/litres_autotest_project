from utils.api_request_with_attach import litres_api_request
from allure_commons._allure import step

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
