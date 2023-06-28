from selenium.webdriver.common.by import By


class HomeLoginPage:

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # locators
    userName = (By.XPATH, "//input[@id='user-name']")
    passWd = (By.XPATH, "//input[@id='password']")
    loginBtn = (By.XPATH, "//input[@id='login-button']")
    loginLocator= By.XPATH, "//input[@id='login-button']"

    # actions
    def setUserName(self):
        return self.driver.find_element(*HomeLoginPage.userName)

    def setPassWd(self):
        return self.driver.find_element(*HomeLoginPage.passWd)

    def clkLoginBtn(self):
        self.driver.find_element(*HomeLoginPage.loginBtn).click()
