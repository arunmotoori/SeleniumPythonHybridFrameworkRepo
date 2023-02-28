import time

import pytest
from selenium import webdriver

from utilities.ReadProperties import ReadProperties

driver = None


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = ReadProperties.get_browser()
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    url = ReadProperties.get_url()
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()

