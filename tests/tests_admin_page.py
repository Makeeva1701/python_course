def test_admin_page_find_username_entry_field(browser, url):
    url = url + "/admin/"
    browser.get(url)
    browser.find_element_by_css_selector("#input-username").click()


def test_admin_page_find_password_entry_field(browser, url):
    url = url + "/admin/"
    browser.get(url)
    browser.find_element_by_css_selector("#input-password").click()


def test_admin_page_find_button_login(browser, url):
    url = url + "/admin/"
    browser.get(url)
    browser.find_element_by_css_selector("button[type=submit]").click()


def test_admin_page_find_forgotten_href(browser, url):
    url = url + "/admin/"
    browser.get(url)
    browser.find_element_by_css_selector('a[href*="route=common/forgotten"]').click()


def test_admin_page_find_opencart_href(browser, url):
    url = url + "/admin/"
    browser.get(url)
    browser.find_element_by_css_selector('a[href*="www.opencart.com"]').click()


def test_admin_page_find_opencart_logo(browser, url):
    url = url + "/admin/"
    browser.get(url)
    browser.find_element_by_css_selector('.navbar-brand').click()
