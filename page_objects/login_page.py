class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def open_login_page(self, url):
        self.browser.get(url + "/index.php?route=account/login")