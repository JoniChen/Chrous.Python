import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class firstTest (unittest.TestCase):

    def test_login(self):
        self.driver = webdriver.Chrome("/Users/joninow/Documents/SeleniumDrivers/chromedriver")
        self.driver.maximize_window()
        self.driver.get("https://chorus.ai/blueprint/211459")
        email = self.driver.find_element_by_name("email")
        email.send_keys("automation@gmail.com")
        loginButton = self.driver.find_element_by_css_selector("div form button")
        loginButton.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME , "password")))
        password = self.driver.find_element_by_name("password")
        password.send_keys("rhrDBWT78iwU")
        continueButton = self.driver.find_element_by_css_selector("button[class='email']")
        continueButton.click()
        # Verify page loaded when logo appears
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR , "li[class='logo']")))
        #Verify calls list populated
        callsList = self.driver.find_elements_by_css_selector("div[class='col-xs overflow-ellipsis'] h4")
        assert callsList.__len__()==4
        #Select first call
        callsList.__getitem__(0).click()
        #Verify play/stop/forward buttons
        playButton = self.driver.find_element_by_css_selector("i[class='icon medium play-button']")
        playButton.click()
        time.sleep(10)
        playButton.click()
        timer = self.driver.find_element_by_css_selector("div[class='timer']")
        #verify call was played
        self.assertNotIn(timer.text , "0:00")
        #share a moment from sepecific location in call

        #click next call / last call button
        forwardButton = self.driver.find_element_by_css_selector("i[class='icon next play-next']")
        forwardButton.click()
        backwardButton = self.driver.find_element_by_css_selector("i[class='icon next  play-previous']")
        backwardButton.click()




