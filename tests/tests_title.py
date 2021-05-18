def test_title(browser, url):
    browser.get(url)
    current_title = browser.title
    assert current_title == "Your Store"
