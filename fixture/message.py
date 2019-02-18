from selenium.webdriver.common.keys import Keys


class MessageHelper:

    def __init__(self, app):
        self.app = app

    def create(self, message):
        driver = self.app.driver
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

