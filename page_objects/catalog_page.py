class CatalogPage:

    def __init__(self, browser):
        self.browser = browser

    def open_catalog_page(self, url):
        self.browser.get(url + "/index.php?route=product/category&path=20")
