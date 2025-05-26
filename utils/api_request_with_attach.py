import json
import logging
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
import allure
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def litres_api_request(path, method='POST', *args, **kwargs):
    with step('API Request'):
        base_url = 'https://api.litres.ru/foundation/api/'
        full_url = base_url + path

        kwargs['timeout'] = (2, 5)

        with requests.Session() as temp_session:
            retries = Retry(
                total=5,
                backoff_factor=1.5,
                status_forcelist=[500, 502, 503, 504],
                allowed_methods=["GET", "POST", "PUT", "DELETE"]
            )
            adapter = HTTPAdapter(max_retries=retries)
            temp_session.mount('https://', adapter)
            temp_session.mount('http://', adapter)

            result = temp_session.request(url=full_url, method=method, *args, **kwargs)

        log_to_allure_api(result)
        log_to_console_api(result)
        return result

def log_to_allure_api(result):
    allure.attach(
        body=f'Method: {result.request.method}\nURL: {result.request.url}',
        name='Request Info',
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )
    allure.attach(
        body=mask_sensitive_data(result.request.body) if result.request.body else '[Empty]',
        name='Request Body',
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )

    allure.attach(
        body=f'Status code: {result.status_code}',
        name='Response status code',
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )

    allure.attach(
        body=json.dumps(json.loads(mask_sensitive_data(result.text)),
                        indent=4, ensure_ascii=False) if result.text else '[Empty]',
        name='Response',
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )

    cookies_dict = mask_sensitive_data_cookies(result.cookies)
    allure.attach(
        body=json.dumps(cookies_dict, indent=4, ensure_ascii=False),
        name='Cookies',
        attachment_type=AttachmentType.TEXT,
        extension='json'
    )

def log_to_console_api(result):
    log_message = f'''
            ==== HTTP Request ====
            Method: {result.request.method}
            URL: {result.request.url}
            Body:
            {mask_sensitive_data(result.request.body)}

            ==== HTTP Response ====
            Status Code: {result.status_code}
            Body:
            {json.dumps(json.loads(mask_sensitive_data(result.text)),
                        indent=4, ensure_ascii=False) if result.text else "None"}

            ==== Cookies ====
            {'\n'.join([f'{key} = {value}' for key, value in mask_sensitive_data_cookies(result.cookies).items()])}
            '''

    logging.info(log_message)

def mask_sensitive_data(body):
    try:
        body_dict = json.loads(body)
        if 'login' in body_dict:
            body_dict['login'] = '********'
        if 'password' in body_dict:
            body_dict['password'] = '********'
        if 'sid' in body_dict.get('payload', {}).get('data', {}):
            body_dict['payload']['data']['sid'] = '********'
        if '__Secure-session_context' in body_dict:
            body_dict['__Secure-session_context'] = '********'
        return json.dumps(body_dict, indent=4, ensure_ascii=False)
    except (json.JSONDecodeError, TypeError):
        return body

def mask_sensitive_data_cookies(cookies):
    cookies_dict = cookies.get_dict()
    if '__Secure-session_context' in cookies_dict:
        cookies_dict['__Secure-session_context'] = '********'
    return cookies_dict