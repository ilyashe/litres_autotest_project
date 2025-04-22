import json
import logging
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
import allure


def litres_api_request(path, method='POST', *args, **kwargs):
    with step('API Request'):
        base_url = 'https://api.litres.ru/foundation/api/'
        full_url = base_url + path
        result = requests.request(url=full_url, method=method, *args, **kwargs)

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
        body=json.dumps(result.json(), indent=4, ensure_ascii=True) if result.text else '[Empty]',
        name='Response',
        attachment_type=AttachmentType.JSON,
        extension='json'
    )

    cookies_dict = {cookie.name: cookie.value for cookie in result.cookies}
    allure.attach(
        body=json.dumps(cookies_dict, indent=4),
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
            {json.dumps(json.loads(result.text), indent=4, ensure_ascii=False) if result.text else "None"}

            ==== Cookies ====
            {'\n'.join([f'{c.name} = {c.value}' for c in result.cookies])}
            '''

    logging.info(log_message)

def mask_sensitive_data(body):
    try:
        body_dict = json.loads(body)
        if 'login' in body_dict:
            body_dict['login'] = '********'
        if 'password' in body_dict:
            body_dict['password'] = '********'
        return json.dumps(body_dict, indent=4, ensure_ascii=False)
    except (json.JSONDecodeError, TypeError):
        return body
