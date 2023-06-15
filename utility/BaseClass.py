import inspect
import logging

import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogGen(self):
        className = inspect.stack()[1][3]
        logger = logging.getLogger(className)
        file = logging.FileHandler(r"C:\Users\Swapnil\PycharmProjects\DemoProjectSwagLabs\Logs\logfile.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s :  %(name)s : %(funcName)s: %(message)s")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger

    def getExplicitWait(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located(locator))
