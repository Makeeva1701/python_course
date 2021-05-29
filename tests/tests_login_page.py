from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage


def test_login_page_find_email_entry_field(browser, url):
    LoginPage(browser).open_login_page(url)
    browser.find_element(By.CSS_SELECTOR, "#input-email").click()


def test_login_page_find_password_entry_field(browser, url):
    LoginPage(browser).open_login_page(url)
    browser.find_element(By.CSS_SELECTOR, "#input-password").click()


def test_login_page_find_forgotten_href(browser, url):
    LoginPage(browser).open_login_page(url)
    browser.find_element(By.CSS_SELECTOR, 'a[href*="route=account/forgotten"]').click()


def test_login_page_find_button_login(browser, url):
    LoginPage(browser).open_login_page(url)
    browser.find_element(By.CSS_SELECTOR, 'input[type=submit]').click()


def test_login_page_find_continue_href(browser, url):
    LoginPage(browser).open_login_page(url)
    browser.find_element(By.CSS_SELECTOR, 'a.btn-primary').click()
