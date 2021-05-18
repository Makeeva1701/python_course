def test_product_card_find_button_add_to_cart(browser, url):
    url = url + "/index.php?route=product/product&path=57&product_id=49"
    browser.get(url)
    browser.find_element_by_css_selector("button#button-cart").click()


def test_product_card_find_button_reviews(browser, url):
    url = url + "/index.php?route=product/product&path=57&product_id=49"
    browser.get(url)
    browser.find_element_by_css_selector('a[href*="#tab-review"]').click()


def test_product_card_find_button_description(browser, url):
    url = url + "/index.php?route=product/product&path=57&product_id=49"
    browser.get(url)
    browser.find_element_by_css_selector('a[href*="#tab-description"]').click()


def test_product_card_find_quantity_entry_field(browser, url):
    url = url + "/index.php?route=product/product&path=57&product_id=49"
    browser.get(url)
    browser.find_element_by_css_selector('#input-quantity').click()


def test_product_card_find_button_home(browser, url):
    url = url + "/index.php?route=product/product&path=57&product_id=49"
    browser.get(url)
    browser.find_element_by_css_selector('a[href*="index.php?route=common/home"]').click()
