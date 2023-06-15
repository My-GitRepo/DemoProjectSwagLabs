import time

from PageObjectClass.OrangeHRM import HomePageHRM
from utility.BaseClass import BaseClass


class TestHRM(BaseClass):

    def test_02(self,setup):
        self.driver=setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        hp=HomePageHRM(self.driver)

        self.getWaits(hp.locator)
        hp.setUserName('Admin')
        hp.setPassWde('admin123')
        hp.clkLoginBtn()
        time.sleep(5)
        self.driver.close()


