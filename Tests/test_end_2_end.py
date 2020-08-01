# Main testing starts from here

import pytest

from TestData.testData import InputData
from Utilities.BaseClass import BaseClass
from pageObjects.homePage import HomePage


class TestOne(BaseClass):

    def test_verifyHomePageTitle(self, getInputData):       # Test method to verify the home page link
        log = self.getLogger()
        log.info("Verifying the Home page link")
        homePage = HomePage(self.driver)
        homePageTitle = homePage.getTitle()
        if homePageTitle != getInputData["homePage_title"]:
            log.debug("Verification Failed: Home Page title is not %r" % getInputData["homePage_title"])
        else:
            log.info("Verification Passed: Home Page title is %r" % getInputData["homePage_title"])

    def test_studioSelectionOperations(self, getInputData):     # Test method to verify various operations on studio page
        log = self.getLogger()
        log.info("Verifying the Workshop page link")
        homePage = HomePage(self.driver)
        workshopPage = homePage.selectWorkshop()
        workshopPageTitle = workshopPage.getWorkshopPageTitle()     # Checking title of studio search page
        if workshopPageTitle != getInputData["workshopPage_title"]:
            log.debug("Verification Failed: Search Studio Page title is not %r" % getInputData["workshopPage_title"])
        else:
            log.info("Verification Passed: Search Studio Page title is %r" % getInputData["workshopPage_title"])

        workshopPage.searchStudio(getInputData["area_code"])        # Searching list of studios in a given area
        details = workshopPage.getStudioDetails()
        name, distance, address, city = details.split("\n")
        log.info("Title of first studio searched is %r" % name)     # Getting details of first studio searched
        log.info("Distance of first studio searched is %r" % distance)

        studioDetailsPage = workshopPage.selectStudio()             # Verifying displayed location name and searched location name is same
        studioName = studioDetailsPage.getStudioName()
        if name == studioName:
            log.info("Displayed location name %r" % studioName + "is same as first searched name %r" % name)
        else:
            log.info("Displayed location name %r" % studioName + "is different from first searched name %r" % name)

        day = getInputData["weekDay"]                               # Getting appointment details on a specific week day
        log.info("Getting details for appointments on %r " % day)
        studioDetailsPage.printMeetings(day)

    @pytest.fixture(params=InputData.testInputData)  # Method to take test input from testData file
    def getInputData(self, request):
        return request.param
