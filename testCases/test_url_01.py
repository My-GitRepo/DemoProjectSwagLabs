import time

from PageObjectClass.HomePage import HomeLoginPage
from utility.BaseClass import BaseClass
from utility.ReadProperties import ReadData


class TestUrl(BaseClass):
    baseUrl = ReadData.readUrl()
    username = ReadData.readUserName()
    passWd = ReadData.readPassWd()

    def test_url(self, setup):
        self.driver = setup  # fixture

        log = self.getLogGen()  # logger
        hp = HomeLoginPage(self.driver)  # PageObjectClass

        log.info('Test case started')
        log.info('Launching Site')
        self.driver.get(self.baseUrl)  # launching web-application

        log.info('printing page title')
        self.getExplicitWait(hp.loginLocator)
        print(self.driver.title)

        if self.driver.title == 'Swag Labs':
            assert True

            log.info('taking screenshot')
            self.driver.save_screenshot(
                r"C:\Users\Swapnil\PycharmProjects\DemoProjectSwagLabs\screenshots\test_url.png")

            log.info('screenshot taken')
        else:
            assert False
        log.info('Test case executed successfully')

        self.driver.close()
