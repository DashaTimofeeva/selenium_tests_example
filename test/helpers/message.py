import time
from selenium.webdriver.common.keys import Keys


class MessageHelper:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver

    def create(self, message):
        driver = self.app.driver
        # click to compose button
        driver.find_element_by_xpath("//div[text()='Compose']").click()
        # enter addressee
        to = self.driver.find_element_by_name("to")
        to.click()
        to.clear()
        to.send_keys(message.addressee)
        # enter theme
        subjectbox = self.driver.find_element_by_name("subjectbox")
        subjectbox.clear()
        subjectbox.send_keys(message.theme)
        # enter message body
        msg_body = self.driver.find_element_by_css_selector("div[aria-label='Message Body']")
        msg_body.click()
        msg_body.send_keys(message.body)
        time.sleep(4)
        # click send
        driver.find_element_by_xpath("//div[text()='Send']").send_keys(Keys.ENTER)
