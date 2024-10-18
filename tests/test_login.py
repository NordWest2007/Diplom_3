from constants import Constants
from locators.feed_locators import FeedLocators
from locators.home_locators import HomeLocators
from locators.profile_locators import ProfileLocators
from pages.login_page import LoginPage


class TestLogin:
    def test_click_account_button(self, driver):
        login = LoginPage(driver)
        login.authentication_user()
        login.wait_element(HomeLocators.ACCOUNT_BUTTON).click()
        login.wait_element(ProfileLocators.SAVE_BUTTON)
        assert driver.current_url == Constants.URL_PROFILE

    def test_click_feed_button(self, driver):
        login = LoginPage(driver)
        login.authentication_user()
        login.wait_element(HomeLocators.FEED_BUTTON).click()
        login.wait_element(FeedLocators.FEED_TEXT)
        assert driver.current_url == Constants.URL_FEED

    def test_exit_account(self, driver):
        login = LoginPage(driver)
        login.authentication_user()
        login.wait_element(HomeLocators.ACCOUNT_BUTTON).click()
        login.wait_element(ProfileLocators.EXIT_BUTTON).click()
        assert driver.current_url == Constants.URL_LOGIN
