from selenium.webdriver.common.by import By

from page_objects.admin_page import AdminPage
from page_objects.elements.AdminLoginForm import AdminLoginForm
from page_objects.products_page import ProductsPage


def test_add_new_item_in_admin(browser, url):
    AdminPage(browser).open_admin_page(url)
    AdminLoginForm(browser).admin_login()
    ProductsPage(browser).open_products_page()
    ProductsPage(browser).add_new_item()


def test_delete_item_in_admin(browser, url):
    AdminPage(browser).open_admin_page(url)
    AdminLoginForm(browser).admin_login()
    ProductsPage(browser).open_products_page()
    ProductsPage(browser).delete_item()


def test_admin_page_find_username_entry_field(browser, url):
    AdminPage(browser).open_admin_page(url)
    browser.find_element(By.CSS_SELECTOR, "#input-username").click()


def test_admin_page_find_password_entry_field(browser, url):
    AdminPage(browser).open_admin_page(url)
    browser.find_element(By.CSS_SELECTOR, "#input-password").click()


def test_admin_page_find_button_login(browser, url):
    AdminPage(browser).open_admin_page(url)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


def test_admin_page_find_forgotten_href(browser, url):
    AdminPage(browser).open_admin_page(url)
    browser.find_element(By.CSS_SELECTOR, 'a[href*="route=common/forgotten"]').click()


def test_admin_page_find_opencart_href(browser, url):
    AdminPage(browser).open_admin_page(url)
    browser.find_element(By.CSS_SELECTOR, 'a[href*="www.opencart.com"]').click()


def test_admin_page_find_opencart_logo(browser, url):
    AdminPage(browser).open_admin_page(url)
    browser.find_element(By.CSS_SELECTOR, '.navbar-brand').click()
