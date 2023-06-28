from selenium.common import NoSuchElementException

from PageObjectClass.HomePage import HomeLoginPage
from PageObjectClass.LoginPage import MainLoginPage
from utility.BaseClass import BaseClass
from utility.ReadProperties import ReadData
from utility.XLUtility import getRowCount, readData, writeData


class TestLoginDDT(BaseClass):
    baseUrl = ReadData.readUrl()
    file = r"C:\Users\Swapnil\PycharmProjects\DemoProjectSwagLabs\TestData\SwagLabs.xlsx"
    rows = getRowCount(file, 'Sheet1')

    def test_login_ddt(self, setup):
        self.driver = setup  # fixture setup

        log = self.getLogGen()  # logger
        hp = HomeLoginPage(self.driver)  # PageObjectClass 0f HomePage
        mp = MainLoginPage(self.driver)  # PageObjectClass 0f login page

        self.driver.get(self.baseUrl)
        log.info('sending data to the application')

        # using for loop to send multiple data to the application
        for r in range(2, self.rows + 1):

            log.info('Data Driven testing started')

            try:
                # reading the data from excel
                xlUsername = readData(self.file, 'Sheet1', r, 1)
                xlPassWd = readData(self.file, 'Sheet1', r, 2)

                # sending data to the application

                self.getExplicitWait(hp.loginLocator)  # explicit wait to solve synchronisation problem

                hp.setUserName().clear()  # clearing the default data
                hp.setUserName().send_keys(xlUsername)  # sending data to the application

                hp.setPassWd().clear()  # clearing the default data
                hp.setPassWd().send_keys(xlPassWd)  # sending data to the application

                hp.clkLoginBtn()

                # validation part
                log.info('validation part started')
                if mp.getCartBtn().is_displayed():
                    assert True
                    writeData(self.file, 'Sheet1', r, 5, 'Pass')  # writing data into excel
                else:
                    assert False
                log.info('validation successful')

                mp.clkMenuBtn()
                mp.clkLogOutBtn()
            except:
                writeData(self.file, 'Sheet1', r, 5, 'Fail')  # writing data into excel
        log.info('Data Driven testing completed')
        self.driver.close()
