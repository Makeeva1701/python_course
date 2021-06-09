from selenium.webdriver.common.by import By

from page_objects.admin_page import AdminPage
from page_objects.elements.AdminLoginForm import AdminLoginForm
from page_objects.products_page import ProductsPage


def test_add_new_item_in_admin(driver, url):
    AdminPage(driver).open_admin_page(url)
    AdminLoginForm(driver).admin_login()
    ProductsPage(driver).open_products_page()
    ProductsPage(driver).add_new_item()


def test_delete_item_in_admin(driver, url):
    AdminPage(driver).open_admin_page(url)
    AdminLoginForm(driver).admin_login()
    ProductsPage(driver).open_products_page()
    ProductsPage(driver).delete_item()


def test_admin_page_find_username_entry_field(driver, url):
    AdminPage(driver).open_admin_page(url)
    driver.find_element(By.CSS_SELECTOR, "#input-username").click()


def test_admin_page_find_password_entry_field(driver, url):
    AdminPage(driver).open_admin_page(url)
    driver.find_element(By.CSS_SELECTOR, "#input-password").click()


def test_admin_page_find_button_login(driver, url):
    AdminPage(driver).open_admin_page(url)
    driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


def test_admin_page_find_forgotten_href(driver, url):
    AdminPage(driver).open_admin_page(url)
    driver.find_element(By.CSS_SELECTOR, 'a[href*="route=common/forgotten"]').click()


def test_admin_page_find_opencart_href(driver, url):
    AdminPage(driver).open_admin_page(url)
    driver.find_element(By.CSS_SELECTOR, 'a[href*="www.opencart.com"]').click()


def test_admin_page_find_opencart_logo(driver, url):
    AdminPage(driver).open_admin_page(url)
    driver.find_element(By.CSS_SELECTOR, '.navbar-brand').click()
