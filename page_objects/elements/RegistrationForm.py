from selenium.webdriver.common.by import By

from extra.utils import generate_password, generate_firstname, generate_lastname, generate_email, generate_phone


class RegistrationForm:
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    INPUT_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "input[value='Continue']")

    def __init__(self, browser):
        self.browser = browser

    def open_registration_form(self, url):
        self.browser.get(url + "/index.php?route=account/register")

    def registration_user(self):
        password = generate_password()
        self.browser.find_element(self.INPUT_FIRSTNAME[0], self.INPUT_FIRSTNAME[1]).send_keys(generate_firstname())
        self.browser.find_element(self.INPUT_LASTNAME[0], self.INPUT_LASTNAME[1]).send_keys(generate_lastname())
        self.browser.find_element(self.INPUT_EMAIL[0], self.INPUT_EMAIL[1]).send_keys(generate_email())
        self.browser.find_element(self.INPUT_TELEPHONE[0], self.INPUT_TELEPHONE[1]).send_keys(generate_phone())
        self.browser.find_element(self.INPUT_PASSWORD[0], self.INPUT_PASSWORD[1]).send_keys(password)
        self.browser.find_element(self.INPUT_CONFIRM[0], self.INPUT_CONFIRM[1]).send_keys(password)
        self.browser.find_element(self.CHECKBOX[0], self.CHECKBOX[1]).click()
        self.browser.find_element(self.BUTTON_CONTINUE[0], self.BUTTON_CONTINUE[1]).click()
