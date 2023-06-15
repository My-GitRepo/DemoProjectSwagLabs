from selenium.webdriver.common.by import By


class HomePageHRM:

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # locators
    userName = (By.XPATH, "//input[@placeholder='Username']")
    passWd = (By.XPATH, "//input[@placeholder='Password']")
    loginBtn = (By.XPATH, "//button[normalize-space()='Login']")
    locator = By.XPATH, "//button[normalize-space()='Login']"
    dashBoard = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    locatorDashBoard = By.XPATH, "//h6[normalize-space()='Dashboard']"

    # actions
    def setUserName(self, username):
        self.driver.find_element(*HomePageHRM.userName).send_keys(username)

    def setPassWde(self, password):
        self.driver.find_element(*HomePageHRM.passWd).send_keys(password)

    def clkLoginBtn(self):
        self.driver.find_element(*HomePageHRM.loginBtn).click()

    def getDashBoard(self):
        self.driver.find_element(*HomePageHRM.dashBoard)
