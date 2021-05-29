from selenium.webdriver.common.by import By

from extra import test_data


class AdminLoginForm:
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[type=submit]")

    def __init__(self, browser):
        self.browser = browser

    def admin_login(self):
        self.browser.find_element(self.INPUT_USERNAME[0], self.INPUT_USERNAME[1]).send_keys(test_data.user_admin['username'])
        self.browser.find_element(self.INPUT_PASSWORD[0], self.INPUT_PASSWORD[1]).send_keys(test_data.user_admin['password'])
        self.browser.find_element(self.BUTTON_SUBMIT[0], self.BUTTON_SUBMIT[1]).click()
