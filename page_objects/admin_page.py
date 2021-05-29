class AdminPage:

    def __init__(self, browser):
        self.browser = browser

    def open_admin_page(self, url):
        self.browser.get(url + "admin/")