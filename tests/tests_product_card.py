from selenium.webdriver.common.by import By

from page_objects.products_card_page import ProductsCardPage


def test_product_card_find_button_add_to_cart(browser, url):
    ProductsCardPage(browser).open_products_card_page(url)
    browser.find_element(By.CSS_SELECTOR, "button#button-cart").click()


def test_product_card_find_button_reviews(browser, url):
    ProductsCardPage(browser).open_products_card_page(url)
    browser.find_element(By.CSS_SELECTOR, 'a[href*="#tab-review"]').click()


def test_product_card_find_button_description(browser, url):
    ProductsCardPage(browser).open_products_card_page(url)
    browser.find_element(By.CSS_SELECTOR, 'a[href*="#tab-description"]').click()


def test_product_card_find_quantity_entry_field(browser, url):
    ProductsCardPage(browser).open_products_card_page(url)
    browser.find_element(By.CSS_SELECTOR, '#input-quantity').click()


def test_product_card_find_button_home(browser, url):
    ProductsCardPage(browser).open_products_card_page(url)
    browser.find_element(By.CSS_SELECTOR, 'a[href*="index.php?route=common/home"]').click()
