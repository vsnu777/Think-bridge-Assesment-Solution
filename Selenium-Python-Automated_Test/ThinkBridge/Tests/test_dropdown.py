import logging
from Configuration.Base import BaseClass
from Pages.loginPage import LoginPage
from TestData import testdata
from Utility import custom_logger as cl
from Utility.teststatus import TestStatus
from testlib.navigation import Navigation


class TestLogin(BaseClass):
    log = cl.customlogger(logging.INFO)
    ts = TestStatus()


    def test_dropdown_validation(self):
        testname = "Dropdown validation on login page"
        nav = Navigation(self.driver)
        ln = LoginPage(self.driver)
        nav.launch_JabaTalks()
        res1 = ln.Verify_dropdowns(testdata.dropdown_items[0])
        self.ts.mark(res1, "Verify that dropdown contains English language")
        res2 = ln.Verify_dropdowns(testdata.dropdown_items[1])
        self.ts.mark(res2, "Verify that dropdown contains Dutch language")
        self.ts.markFinal(testname)
