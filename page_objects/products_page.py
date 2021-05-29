from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from extra.utils import generate_text


class ProductsPage:
    BUTTON_CATALOG = (By.CSS_SELECTOR, 'a[href*=collapse1]')
    BUTTON_PRODUCTS = (By.CSS_SELECTOR, "a[href*=product]")
    BUTTON_ADD_NEW_ITEM = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    FIELD_NAME_1 = (By.CSS_SELECTOR, "#input-name1")
    FIELD_META_TITLE = (By.CSS_SELECTOR, "#input-meta-title1")
    BUTTON_DATA = (By.CSS_SELECTOR, "a[href*=tab-data]")
    FIELD_MODEL = (By.CSS_SELECTOR, "#input-model")
    BUTTON_SAVE = (By.CSS_SELECTOR, "[data-original-title=Save]")
    CHECKBOX_ITEM = (By.CSS_SELECTOR, "input[type=checkbox]")
    BUTTON_DELETE = (By.CSS_SELECTOR, "[data-original-title=Delete]")

    def __init__(self, browser):
        self.browser = browser

    def open_products_page(self):
        self.browser.find_elements(self.BUTTON_CATALOG[0], self.BUTTON_CATALOG[1])[0].click()
        button = self.browser.find_element(self.BUTTON_PRODUCTS[0], self.BUTTON_PRODUCTS[1])
        self.browser.implicitly_wait(1)
        ActionChains(self.browser).move_to_element(button).click(button).perform()

    def add_new_item(self):
        self.browser.find_element(self.BUTTON_ADD_NEW_ITEM[0], self.BUTTON_ADD_NEW_ITEM[1]).click()
        self.browser.find_element(self.FIELD_NAME_1[0], self.FIELD_NAME_1[1]).send_keys(generate_text())
        self.browser.find_element(self.FIELD_META_TITLE[0], self.FIELD_META_TITLE[1]).send_keys(generate_text())
        self.browser.find_element(self.BUTTON_DATA[0], self.BUTTON_DATA[1]).click()
        self.browser.find_element(self.FIELD_MODEL[0], self.FIELD_MODEL[1]).send_keys(generate_text())
        self.browser.find_element(self.BUTTON_SAVE[0], self.BUTTON_SAVE[1]).click()

    def delete_item(self):
        self.browser.find_elements(self.CHECKBOX_ITEM[0], self.CHECKBOX_ITEM[1])[1].click()
        self.browser.find_element(self.BUTTON_DELETE[0], self.BUTTON_DELETE[1]).click()
        alert = self.browser.switch_to.alert
        alert.accept()
