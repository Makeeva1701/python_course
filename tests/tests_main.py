from selenium.webdriver.common.by import By


def test_main_page_find_buy_button_in_product_card(browser, url):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, "button[onclick*=cart]").click()


def test_main_page_find_heart_icon_in_header(browser, url):
    browser.get(url)
    browser.find_elements(By.CSS_SELECTOR, "i.fa-heart")[0].click()


def test_main_page_find_heart_button_in_product_card(browser, url):
    browser.get(url)
    browser.find_elements(By.CSS_SELECTOR, "i.fa-heart")[1].click()


def test_main_page_find_foto_in_product_card(browser, url):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, 'img[src*="apple_cinema_30-200x200.jpg"]').click()


def test_main_page_find_basket(browser, url):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, '#cart-total').click()

