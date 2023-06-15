import time

from PageObjectClass.LoginPage import HomeLoginPage
from utility.BaseClass import BaseClass
from utility.ReadProperties import ReadData


class TestUrl(BaseClass):
    baseUrl = ReadData.readUrl()
    username = ReadData.readUserName()
    passWd = ReadData.readPassWd()

    def test_url_login(self, setup):
        self.driver = setup  # fixture

        self.driver.get(self.baseUrl)  # launching web-application

        hp = HomeLoginPage(self.driver)  # PageObjectClass

        self.getWaits(hp.loginLocator)
        print(self.driver.title)

        hp.setUserName(self.username)  # sending data from config file
        hp.setPassWd(self.passWd)  # sending data from config file

        self.driver.save_screenshot(
            r"C:\Users\Swapnil\PycharmProjects\DemoProjectSwagLabs\screenshots\test_url_login.png")

        hp.clkLoginBtn()

        print(self.driver.title)
        time.sleep(5)
        self.driver.close()
