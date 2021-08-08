import logging
from Configuration.Base import BaseClass
from Pages.Signup import SignupPage
from Pages.loginPage import LoginPage
from Utility import custom_logger as cl
from Utility.teststatus import TestStatus
from testlib.navigation import Navigation


class TestSignup(BaseClass):
    log = cl.customlogger(logging.INFO)
    ts = TestStatus()

    def test_dropdown_validation(self):
        testname = "Receiving email verification"
        nav = Navigation(self.driver)
        ln = LoginPage(self.driver)
        sn = SignupPage(self.driver)
        nav.launch_JabaTalks()
        ln.send_email()
        res = sn.verifyEmail()
        self.ts.mark(res, "Verify that email has been received successfully")
        self.ts.markFinal(testname)
