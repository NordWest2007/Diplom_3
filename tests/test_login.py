import allure

from constants import Constants
from locators.feed_locators import FeedLocators
from locators.home_locators import HomeLocators
from locators.profile_locators import ProfileLocators
from pages.login_page import LoginPage


@allure.feature("Личный кабинет")
class TestLogin:
    @allure.title("переход по клику на «Личный кабинет»")
    def test_click_account_button(self, driver):
        login = LoginPage(driver)
        login.authentication_user()
        login.wait_element(HomeLocators.ACCOUNT_BUTTON).click()
        login.wait_element(ProfileLocators.SAVE_BUTTON)
        assert driver.current_url == Constants.URL_PROFILE

    @allure.title("переход в раздел «История заказов»")
    def test_click_history_button(self, driver):
        login = LoginPage(driver)
        login.authentication_user()
        login.wait_element(ProfileLocators.HISTORY_BUTTON).click()
        assert driver.current_url == Constants.URL_HISTORY

    @allure.title("выход из аккаунта")
    def test_exit_account(self, driver):
        login = LoginPage(driver)
        login.authentication_user()
        login.wait_element(HomeLocators.ACCOUNT_BUTTON).click()
        login.wait_element(ProfileLocators.EXIT_BUTTON).click()
        assert driver.current_url == Constants.URL_LOGIN
