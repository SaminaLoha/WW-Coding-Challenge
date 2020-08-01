# This file contains elements and methods for Home Page

from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass
from pageObjects.workshopPage import WorkshopPage


class HomePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
    workshop =(By.CLASS_NAME,"find-a-meeting")

    def getTitle(self):         # Method to get home page title
       return self.driver.title

    def selectWorkshop(self):   # Method to click on Find a Workshop link and navigate to that page
        self.driver.find_element(*HomePage.workshop).click()
        self.verifyElementPresence(By.ID, "location-search")
        workshopPage = WorkshopPage(self.driver)
        return workshopPage




