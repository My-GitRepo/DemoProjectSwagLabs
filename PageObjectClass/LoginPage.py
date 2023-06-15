from selenium.webdriver.common.by import By


class MainLoginPage:

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # locator

    cartBtn = (By.XPATH, "//a[@class='shopping_cart_link']")
    menuBtn = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    logOutBtn = (By.XPATH, "//a[@id='logout_sidebar_link']")
    loginLocator = By.XPATH, "//input[@id='login-button']"
    cartLocator = By.XPATH, "//a[@class='shopping_cart_link']"

    # actions

    def getCartBtn(self):
        return self.driver.find_element(*MainLoginPage.cartBtn)

    def clkMenuBtn(self):
        self.driver.find_element(*MainLoginPage.menuBtn).click()

    def clkLogOutBtn(self):
        self.driver.find_element(*MainLoginPage.logOutBtn).click()
