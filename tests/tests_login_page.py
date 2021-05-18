import time


def test_login_page_find_email_entry_field(browser, url):
    url = url + "/index.php?route=account/login"
    browser.get(url)
    browser.find_element_by_css_selector("#input-email").click()


def test_login_page_find_password_entry_field(browser, url):
    url = url + "/index.php?route=account/login"
    browser.get(url)
    browser.find_element_by_css_selector("#input-password").click()


def test_login_page_find_forgotten_href(browser, url):
    url = url + "/index.php?route=account/login"
    browser.get(url)
    browser.find_element_by_css_selector('a[href*="route=account/forgotten"]').click()


def test_login_page_find_button_login(browser, url):
    url = url + "/index.php?route=account/login"
    browser.get(url)
    browser.find_element_by_css_selector('input[type=submit]').click()


def test_login_page_find_continue_href(browser, url):
    url = url + "/index.php?route=account/login"
    browser.get(url)
    browser.find_element_by_css_selector('a.btn-primary').click()
