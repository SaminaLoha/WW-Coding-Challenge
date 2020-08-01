# This file contains elements and methods for Studio/ Workshop Search Page

from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass
from pageObjects.studioDetailsPage import StudioDetailsPage


class WorkshopPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    location = (By.ID, "location-search")       # Various element selectors from page
    button = (By.ID, "location-search-cta")
    studios = (By.ID, "search-results")
    studio_title = (By.XPATH, "div[1]/a")

    def getWorkshopPageTitle(self):             # Method to get Studio Search Page title
        return self.driver.title

    def searchStudio(self, search_string):      # Method to search a studio as per area code
                                                # search_string here can be pincode, city, etc.
        self.driver.find_element(*WorkshopPage.location).send_keys(search_string)
        self.driver.find_element(*WorkshopPage.button).click()

    def getStudioDetails(self):                 # Method to get details about first studio resulted from the search
        self.verifyElementPresence(By.ID, "search-results")
        studio = self.driver.find_element(*WorkshopPage.studios)
        details = studio.find_element(*WorkshopPage.studio_title).text
        return details

    def selectStudio(self):                 # Method to select first studio and navigating to specific studio page
        studio = self.driver.find_element(*WorkshopPage.studios)
        studio.find_element(*WorkshopPage.studio_title).click()
        self.verifyElementPresence(By.TAG_NAME, "h1")
        studioDetailsPage = StudioDetailsPage(self.driver)
        return studioDetailsPage

