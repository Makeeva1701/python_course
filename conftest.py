import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--executor", action="store", default="192.168.0.80")
    parser.addoption("--url", default="http://localhost/")


@pytest.fixture(scope="function")
def url(request):
    return request.config.getoption("url")


@pytest.fixture
def firefox(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def chrome(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    wd = webdriver.Remote(
        command_executor=f"http://{executor}:4444/",
        desired_capabilities={"browserName": browser}
    )
    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd
