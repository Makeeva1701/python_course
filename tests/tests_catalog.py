def test_catalog_page_find_button_last_view(browser, url):
    url = url + "/index.php?route=product/category&path=20"
    browser.get(url)
    browser.find_element_by_css_selector("#list-view").click()


def test_catalog_page_find_button_grid_view(browser, url):
    url = url + "/index.php?route=product/category&path=20"
    browser.get(url)
    browser.find_element_by_css_selector("#grid-view").click()


def test_catalog_page_find_button_input_sort(browser, url):
    url = url + "/index.php?route=product/category&path=20"
    browser.get(url)
    browser.find_element_by_css_selector("#input-sort").click()


def test_catalog_page_find_button_input_limit(browser, url):
    url = url + "/index.php?route=product/category&path=20"
    browser.get(url)
    browser.find_element_by_css_selector("#input-limit").click()


def test_catalog_page_find_button_icon_heart(browser, url):
    url = url + "/index.php?route=product/category&path=20"
    browser.get(url)
    browser.find_elements_by_css_selector("i.fa-heart")[1].click()


def test_catalog_page_find_button_pc_in_listing(browser, url):
    url = url + "/index.php?route=product/category&path=20"
    browser.get(url)
    browser.find_elements_by_css_selector('a[href*="20_26"]')[2].click()


def test_catalog_page_find_button_mac_in_listing(browser, url):
    url = url + "/index.php?route=product/category&path=20"
    browser.get(url)
    browser.find_elements_by_css_selector('a[href*="20_27"]')[2].click()
