import logging
from Utility import custom_logger as cl
from Utility.ReadProperty import ReadConfig
from selenium.webdriver.common.by import By

class Navigation:
    def __init__(self, driver):
        self.driver = driver
        self.log = cl.customlogger(logging.INFO)

    def select_language_dropdown(self):
        """This method clicks language dropdown"""
        language_dropdown = self.driver.find_element(By.CSS_SELECTOR, ".language-box")
        language_dropdown.click()

    def launch_JabaTalks(self):
        """This method launches the JabaTalks website"""
        application_url = ReadConfig.getApplicationUrl()
        self.driver.get(application_url)
        self.log.info("Opened JabaTalks")
        self.driver.maximize_window()

    def launch_SharkEmail(self):
        """This method launches the SharkEmail"""
        sharkemail_url = ReadConfig.getSharkEmailUrl()
        self.driver.get(sharkemail_url)
        self.log.info("Opened JabaTalks")
        self.driver.maximize_window()