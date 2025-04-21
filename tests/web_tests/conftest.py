import pytest
from selene import browser
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from utils import attach

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def setting_browser():
    browser_version = os.getenv('browser_version', '128.0')
    browser.config.base_url = 'https://www.litres.ru/'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    options = Options()
    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': browser_version,
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }

    selenoid_login = os.getenv('SELENOID_LOGIN')
    selenoid_pass = os.getenv('SELENOID_PASS')
    selenoid_url = os.getenv('SELENOID_URL')

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f'https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub',
        options=options)

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser, selenoid_url)

    browser.quit()