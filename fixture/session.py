from selenium.webdriver.common.keys import Keys


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        driver = self.app.driver
        self.app.open_home_page()
        # enter login
        driver.find_element_by_id("identifierId").click()
        driver.find_element_by_id("identifierId").clear()
        driver.find_element_by_id("identifierId").send_keys(login)
        driver.find_element_by_id("identifierId").send_keys(Keys.ENTER)
        # enter password
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.implicitly_wait(15)

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//header[@id='gb']/div[2]/div[3]/div/div[2]/div/a/span").click()
        driver.find_element_by_id("gb_71").click()
