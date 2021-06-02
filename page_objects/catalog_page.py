from extra.test_data import catalog_id


class CatalogPage:

    def __init__(self, browser):
        self.browser = browser

    def open_catalog_page(self, url):
        self.browser.get(url + f"/index.php?route=product/category&path={catalog_id}")
