from extra.test_data import product_id


class ProductsCardPage:

    def __init__(self, browser):
        self.browser = browser

    def open_products_card_page(self, url):
        self.browser.get(url + f"/index.php?route=product/product&path=57&product_id={product_id}")
