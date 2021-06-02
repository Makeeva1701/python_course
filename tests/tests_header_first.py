from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_currency_switching(browser, url):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, "i.fa.fa-caret-down").click()
    button = browser.find_element(By.CSS_SELECTOR, 'button[name=EUR]')
    browser.implicitly_wait(1)
    ActionChains(browser).move_to_element(button).click(button).perform()
