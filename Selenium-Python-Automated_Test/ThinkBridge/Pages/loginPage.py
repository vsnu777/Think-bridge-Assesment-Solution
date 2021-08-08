import logging
import time
from TestData import testdata
from Utility import custom_logger as cl
from testlib.commontestlib import Common_lib
from testlib.navigation import Navigation


class LoginPage:
    log = cl.customlogger(logging.INFO)
    name_field_id = "name"
    org_field_id = "orgName"
    email_field_name = "email"
    accept_checkbox_xpath = "//label[@class='ui-checkbox']//span"
    submit_button_css = "button[type='submit']"

    def __init__(self, driver):
        self.driver = driver
        self.nav = Navigation(driver)
        self.clib = Common_lib(driver)


    def Verify_dropdowns(self,exp_lang):
        """This method verifies the dropdowns in Jabatalks login page"""
        self.nav.select_language_dropdown()
        dropdown_elements = self.clib.getElementList(".ui-select-choices-row-inner div","css")
        if len(dropdown_elements) > 0:
            for language in dropdown_elements:
                lang = language.text
                if lang == exp_lang:
                    self.log.info("dropdown has %s language menu item",exp_lang)
                    break
            else:
                self.log.error("dropdown does not have %s language menu item",exp_lang)
                return False
            return True
        else:
            self.log.error("Dropdown does not have any value")
            return False


    def send_email(self):
        name_field = self.clib.getElement(locator=self.name_field_id,locatorType="id")
        name_field.send_keys(testdata.user_name)
        self.log.info("Entered Name")
        org_field = self.clib.getElement(locator=self.org_field_id, locatorType="id")
        org_field.send_keys(testdata.organization_name)
        self.log.info("Entered organization Name")
        email_field = self.clib.getElement(locator=self.email_field_name, locatorType="name")
        email_field.send_keys(testdata.email_id)
        self.log.info("Entered email")
        accept_checkbox = self.clib.getElement(locator=self.accept_checkbox_xpath, locatorType="xpath")
        accept_checkbox.click()
        self.log.info("Clicked on I agree to the Terms And Conditions checkbox")
        submit_button = self.clib.getElement(locator=self.submit_button_css, locatorType="css")
        submit_button.click()
        self.log.info("Clicked on Get Started button")






