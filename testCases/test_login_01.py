from PageObjectClass.HomePage import HomeLoginPage
from PageObjectClass.LoginPage import MainLoginPage
from utility.BaseClass import BaseClass
from utility.ReadProperties import ReadData


class TestLoginFunc(BaseClass):
    baseUrl = ReadData.readUrl()
    username = ReadData.readUserName()
    passWd = ReadData.readPassWd()

    def test_login(self, setup):
        self.driver = setup  # fixture
        log = self.getLogGen()
        hp = HomeLoginPage(self.driver)  # PageObjectClass 0f Home Page
        mp = MainLoginPage(self.driver)  # PageObjectClass 0f Login Page

        log.info('Launching application')
        log.info('Login test case started')

        self.driver.get(self.baseUrl)  # launching web-application

        self.getExplicitWait(hp.loginLocator)  # explicit wait
        hp.setUserName(self.username)
        hp.setPassWd(self.passWd)
        hp.clkLoginBtn()
        log.info('clicked on login btn')

        self.getExplicitWait(mp.cartLocator)  # explicit wait

        # validation part
        if mp.getCartBtn().is_displayed():
            assert True
            self.driver.save_screenshot(
                r"C:\Users\Swapnil\PycharmProjects\DemoProjectSwagLabs\screenshots\test_login.png")

        else:
            assert False
        log.info('Validation Successfull')

        mp.clkMenuBtn()
        mp.clkLogOutBtn()
        self.driver.close()

