import logging
from traceback import print_stack

from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from TestData import testdata
from Utility import custom_logger as cl

from selenium.webdriver.support.wait import WebDriverWait

from testlib.navigation import Navigation


class Common_lib:
    log = cl.customlogger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        self.nav = Navigation(driver)

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and locatorType: " + locatorType)
        return element

    def waitForElement(self,
                       timeout=10, pollFrequency=0.5):
        wait = None
        try:

            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
        except:
            self.log.info("exception occured")
            print_stack()
        return wait

    def set_tempEmail(self):
        self.nav.launch_SharkEmail()
        wait = self.waitForElement(timeout=20)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#gm-host-select")))
        self.log.info("Launch SharkEmail")
        select_editbox = self.getElement(locator="inbox-id", locatorType="id").click()
        edit_email = self.getElement(locator="#inbox-id input[type=text]", locatorType="css")
        edit_email.clear()
        self.log.info("Cleared previous text")
        edit_email.send_keys(testdata.email_name)
        self.log.info("Set email name")
        save_email = self.getElement(".save", "css")
        save_email.click()
        self.log.info("Saved email")
