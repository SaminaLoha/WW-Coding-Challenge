# This file contains the Base Class which is inherited by other classes
# It contains a methods for configuring logging and another method to wait till an elements presence is located
import inspect
import logging

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    # Method to configure logging
    def getLogger(self):
        loggername = inspect.stack()[1][3]  # this will give test case name
        logger = logging.getLogger(loggername)

        fileHandler = logging.FileHandler('logfile.log')
        # %(variables)s - this means it will get evaluated at runtime
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object, in which file to print

        # below is the order for logging level
        logger.setLevel(logging.INFO)  # all data from level info will be printed
        return logger

    def verifyElementPresence(self, locator, locator_value):    # Method for wait
        wait = WebDriverWait(self.driver, 40)
        wait.until(expected_conditions.presence_of_element_located((locator, locator_value)))