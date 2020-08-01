# This file contains elements and methods for a specific Studio Page

from collections import defaultdict
from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass


class StudioDetailsPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    studioName = (By.TAG_NAME, "h1")
    schedules = (By.XPATH, "//div[contains(@class, 'day-')]")

    def getStudioName(self):        # Method to get name of the Studio
        studioName = self.driver.find_element(*StudioDetailsPage.studioName).text
        return studioName

    def printMeetings(self, weekDay):       # Method to print appointment details
        days = self.driver.find_elements(*StudioDetailsPage.schedules)
        personDetails = defaultdict(int)    # Dictionary to save person and number of appointments in a day
        log = self.getLogger()

        for day in days:
            dayName = day.find_element_by_xpath("span").text
            if dayName == weekDay:
                meeting_schedules = day.find_elements_by_xpath("div")
                if not meeting_schedules:
                    break
                else:
                    for meeting in meeting_schedules:
                        person_name = meeting.find_element_by_xpath("span[2]").text
                        personDetails[person_name] += 1
        if not personDetails:
            log.info("No appointments scheduled for %r" % weekDay)
        else:
            for person in personDetails:
                log.info("%r" % person + "-" + "%r" % str(personDetails[person]))

