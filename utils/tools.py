from selene import browser
import os
import tests

def open_new_window(window_number):
    window_handles = browser.driver.window_handles
    browser.driver.switch_to.window(window_handles[window_number])

def path_to_apk(file_name):
    return os.path.abspath(
        os.path.join(os.path.dirname(tests.__file__), f'../apk/{file_name}')
    )