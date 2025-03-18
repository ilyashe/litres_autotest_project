from selene import browser


def open_new_window(window_number):
    window_handles = browser.driver.window_handles
    browser.driver.switch_to.window(window_handles[window_number])