from selenium.webdriver.common.by import By

from page_objects.catalog_page import CatalogPage


def test_catalog_page_find_button_last_view(browser, url):
    CatalogPage(browser).open_catalog_page(url)
    browser.find_element(By.CSS_SELECTOR, "#list-view").click()


def test_catalog_page_find_button_grid_view(browser, url):
    CatalogPage(browser).open_catalog_page(url)
    browser.find_element(By.CSS_SELECTOR, "#grid-view").click()


def test_catalog_page_find_button_input_sort(browser, url):
    CatalogPage(browser).open_catalog_page(url)
    browser.find_element(By.CSS_SELECTOR, "#input-sort").click()


def test_catalog_page_find_button_input_limit(browser, url):
    CatalogPage(browser).open_catalog_page(url)
    browser.find_element(By.CSS_SELECTOR, "#input-limit").click()


def test_catalog_page_find_button_icon_heart(browser, url):
    CatalogPage(browser).open_catalog_page(url)
    browser.find_elements(By.CSS_SELECTOR, "i.fa-heart")[1].click()


def test_catalog_page_find_button_pc_in_listing(browser, url):
    CatalogPage(browser).open_catalog_page(url)
    browser.find_elements(By.CSS_SELECTOR, 'a[href*="20_26"]')[2].click()


def test_catalog_page_find_button_mac_in_listing(browser, url):
    CatalogPage(browser).open_catalog_page(url)
    browser.find_elements(By.CSS_SELECTOR, 'a[href*="20_27"]')[2].click()
