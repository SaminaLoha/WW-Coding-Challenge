import time
from collections import defaultdict

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.weightwatchers.com/us//")
print(driver.title)
driver.find_element_by_class_name("find-a-meeting").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.ID,"location-search")))
print(driver.title)
driver.find_element_by_id("location-search").send_keys("10011")
driver.find_element_by_id("location-search-cta").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.ID,"search-results")))

studios = driver.find_element_by_id("search-results")
details = studios.find_element_by_xpath("div[1]/a").text
name, dist, add, city = details.split("\n")
print(name)
print(dist)
studios.find_element_by_xpath("div[1]/a").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME,"h1")))
print(driver.find_element_by_tag_name("h1").text)
days = driver.find_elements_by_xpath("//div[contains(@class, 'day-')]")
d = defaultdict(int)
for day in days:
    dayName = day.find_element_by_xpath("span").text
    if dayName == "THU":
        meeting_schedules = day.find_elements_by_xpath("div")
        if not meeting_schedules:
            print("No meetings scheduled for THU")
        else:
            for meeting in meeting_schedules:
                person_name = meeting.find_element_by_xpath("span[2]").text
                d[person_name]+=1

for person in d:
    print(person + "-" + str(d[person]))







#driver.close()
