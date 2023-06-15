import pytest

from selenium import webdriver


@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Chrome()
    # driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    return driver
