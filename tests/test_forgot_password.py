from time import sleep

from constants import Constants
from locators.login_locators import LoginLocators
from pages.login_page import LoginPage


class TestForgotPassword:
    def test_click_forgot_password(self, driver):
        login = LoginPage(driver)
        login.get_url(Constants.URL_LOGIN)
        login.click_on_element(LoginLocators.FORGOT_LINK)
        assert driver.current_url == Constants.URL_FORGOT_PASSWORD

    def test_input_email(self, driver):
        login = LoginPage(driver)
        login.get_url(Constants.URL_FORGOT_PASSWORD)
        login.set_text_to_element(LoginLocators.NAME_FIELD, LoginLocators.EMAIL)
        login.click_on_element_without_wait(LoginLocators.RESTORE_BUTTON)
        login.wait_element(LoginLocators.SAVE_BUTTON)
        assert driver.current_url == Constants.URL_RESET_PASSWORD

    def test_click_view_password(self, driver):
        login = LoginPage(driver)
        login.get_url(Constants.URL_LOGIN)
        login.set_text_to_element(LoginLocators.PASSWORD_NOT_VIEW_FIELD,'mypassword')
        login.wait_element(LoginLocators.PASSWORD_VIEW).click()
        assert login.wait_element(LoginLocators.VIEW_PASSWORD_FIELD)

