import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Chrome()
    # driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    return driver



