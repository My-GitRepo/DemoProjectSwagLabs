import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        print('Launching Chrome')
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        print('Launching Firefox')
    elif browser == 'edge':
        driver = webdriver.Edge()
        driver.maximize_window()
        print('Launching Edge')
    else:
        print('Running in headless browser mode')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)

    return driver
