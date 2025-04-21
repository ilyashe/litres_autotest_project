from selene import browser
import requests
import json

def open_new_window(window_number):
    window_handles = browser.driver.window_handles
    browser.driver.switch_to.window(window_handles[window_number])

def auth_cookie_via_api():
    url = "https://api.litres.ru/foundation/api/auth/login"

    payload = json.dumps({
        "login": "andrey.sokolov11123@gmail.com",
        "password": "andrey4576"
    })
    headers = {
        'app-id': '115'
    }

    result = requests.request("POST", url, headers=headers, data=payload)

    cookie = result.headers.get('request-session-id')
    return cookie