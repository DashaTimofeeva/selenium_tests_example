from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome('/Users/dasha/GitHub/selenium_tests_example/chromedriver')
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("https://mail.google.com/")



    def create_message(self, message):
        driver = self.driver
        # click to compose button
        driver.find_element_by_xpath('//*[@id=":3t"]/div/div').click()
        # enter addressee
        driver.find_element_by_name("to").click()
        driver.find_element_by_name("to").clear()
        driver.find_element_by_name("to").send_keys(message.addressee)
        # enter theme
        driver.find_element_by_name("subjectbox").clear()
        driver.find_element_by_name("subjectbox").send_keys(message.theme)
        # enter message body
        driver.find_element_by_css_selector("div[aria-label='Message Body']").click()
        driver.find_element_by_css_selector("div[aria-label='Message Body']").send_keys(message.body)
        # click send
        driver.find_element_by_xpath("//div[text()='Send']").send_keys(Keys.ENTER)



    def destroy(self):
        self.driver.quit()
