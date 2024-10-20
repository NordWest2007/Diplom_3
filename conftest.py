import allure
import pytest
from selenium import webdriver

from constants import Constants
from locators.home_locators import HomeLocators
from locators.login_locators import LoginLocators
from pages.login_page import LoginPage


@allure.step("Тест запускается в {params}")
@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    driver = None
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    elif request.param == 'Firefox':
        driver = webdriver.Firefox()
    else:
        ValueError('driver error')
    yield driver

    driver.quit()

@pytest.fixture()
def authentication_user(driver):
        login = LoginPage(driver)
        login.get_url(Constants.URL_LOGIN)
        login.set_text_to_element(LoginLocators.EMAIL_FIELD, LoginLocators.EMAIL)
        login.set_text_to_element(LoginLocators.PASSWORD_FIELD, LoginLocators.PASSWORD)
        login.click_on_element_without_wait(LoginLocators.ENTER_BUTTON)
        login.wait_element(HomeLocators.ENTER_BUTTON)