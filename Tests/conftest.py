# Config file for setting Chrome driver and navigating to home page link
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.weightwatchers.com/us//")
    request.cls.driver = driver  # assigning to class driver
    yield
    driver.close()
