from selenium import webdriver
from test.helpers.message import MessageHelper
from test.helpers.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome('/Users/dasha/GitHub/selenium_tests_example/chromedriver')
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.message = MessageHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("https://mail.google.com/")

    def destroy(self):
        self.driver.quit()
