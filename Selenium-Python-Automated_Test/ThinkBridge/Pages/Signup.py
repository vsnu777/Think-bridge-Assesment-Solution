import logging
import time
from Utility import custom_logger as cl
from testlib.commontestlib import Common_lib
from testlib.navigation import Navigation


class SignupPage:
    log = cl.customlogger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        self.nav = Navigation(driver)
        self.clib = Common_lib(driver)

    def setemail(self):
        self.clib.set_tempEmail()


    def verifyEmail(self):
        self.setemail()
        self.log.info("logging in shark email")
        time.sleep(120)
        exp_email = "@jabatalks.com"
        email_list = self.clib.getElementList(locator='.mail_row', locatorType="css")
        self.log.info("emails %s", len(email_list))
        if len(email_list) > 0:
            for email in email_list:
                self.log.info("%s",email.text)
                if exp_email in email.text:
                    self.log.info("Received email successfully")
                    break
            else:
                self.log.info("There is some error, could not recieve email from JabaTalks")
                return False
        else:
            self.log.info("There is some error, we did not receive any email")
            return False
        return True



