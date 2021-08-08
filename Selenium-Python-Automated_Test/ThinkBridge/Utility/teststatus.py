"""
It provides functionality to assert the result
"""
from Configuration.Base import BaseClass

import Utility.custom_logger as cl
import logging

from traceback import print_stack




class TestStatus(BaseClass):
    log = cl.customlogger(logging.INFO)

    def __init__(self):
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: " + resultMessage)

            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: " + resultMessage)

        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName):
        """
        Mark the final result of the verification point in a test case
        """
        pass_list = []
        fail_list = []
        for status in self.resultList:
            if "PASS" in status:
                pass_list.append(status)
            else:
                fail_list.append(status)

        self.log.info("No of Test Passed: %d", len(pass_list))
        self.log.info("No of Test Failed: %d", len(fail_list))

        if len(fail_list) != 0:
            self.log.error(testName + "  ### TEST FAILED")
            assert True == False

        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            assert True == True
