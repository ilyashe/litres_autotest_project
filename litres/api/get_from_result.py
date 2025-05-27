from allure_commons._allure import step


def get_session_id_from_api(result):
    with step('Получение session_id'):
        session_id = result.headers.get('request-session-id')
        return session_id

def get_bsk_cookie_from_api(result):
    with step('Получение BSK cookie'):
        bsk_cookie = result.cookies.get('BSK')
        return bsk_cookie
