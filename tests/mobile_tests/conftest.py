import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
from mobile_config import config
from utils import mobile_attach, tools
from appium import webdriver


@pytest.fixture(scope='function')
def android_management():
    options_dict = {
        'app': config.app if config.app.startswith('bs://')
        else tools.path_to_apk(config.app),
        'appPackage': 'ru.litres.android',
        'appActivity': 'ru.litres.android.splash.MainSplashAlias',
        'appWaitActivity': 'ru.litres.android.splash.*'
    }

    if config.udid:
        options_dict['udid'] = config.udid
    if config.deviceName:
        options_dict['deviceName'] = config.deviceName
    if config.platformVersion:
        options_dict['platformVersion'] = config.platformVersion

    options = UiAutomator2Options().load_capabilities(options_dict)

    if config.context == 'bstack':
        options.set_capability('bstack:options', {
            'projectName': 'Litres autotest project',
            'buildName': 'litres-build-1',
            'sessionName': 'BStack litres_test',
            'userName': config.bstack_userName,
            'accessKey': config.bstack_accessKey,
        })

    with allure.step('Инициализация сессии'):
        browser.config.driver = webdriver.Remote(
            config.remote_url,
            options=options
        )

    browser.config.timeout = config.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield
    mobile_attach.attach_screenshot(browser)
    mobile_attach.attach_xml(browser)

    session_id = browser.driver.session_id

    with allure.step('Завершение сессии'):
        browser.quit()

    if config.context == 'bstack':
        mobile_attach.attach_bstack_video(session_id)
