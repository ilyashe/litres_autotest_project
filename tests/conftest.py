import pytest
from selene import browser
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def setting_browser():

    browser.config.base_url = 'https://www.litres.ru/'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    browser.quit()