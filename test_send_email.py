# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

from message import Message


class SendEmail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/dasha/GitHub/selenium_tests_example/chromedriver')
        self.driver.implicitly_wait(30)

    def test_send_message(self):
        driver = self.driver
        self.login(driver, login="dariatimofeevatest@gmail.com", password="Bl@Sl56Er23!!7")
        self.create_message(driver, Message(addressee="timofeyevadasha@gmail.com", theme="test", body="test"))
        self.logout(driver)

    def test_send_empty_message(self):
        driver = self.driver
        self.login(driver, login="dariatimofeevatest@gmail.com", password="Bl@Sl56Er23!!7")
        self.create_message(driver, Message(addressee="timofeyevadasha@gmail.com", theme="test", body=""))
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_xpath("//header[@id='gb']/div[2]/div[3]/div/div[2]/div/a/span").click()
        driver.find_element_by_id("gb_71").click()

    def create_message(self, driver, message):
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

    def login(self, driver, login, password):
        self.open_home_page(driver)
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

    def open_home_page(self, driver):
        driver.get("https://mail.google.com/")

    def tearDown(self):
        self.driver.quit()
