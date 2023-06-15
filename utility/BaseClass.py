import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getWaits(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located(locator))
