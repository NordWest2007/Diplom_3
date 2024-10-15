import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver_chrome = webdriver.Firefox()
    yield driver_chrome

    driver_chrome.quit()
