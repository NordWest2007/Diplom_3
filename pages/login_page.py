from constants import Constants
from locators.home_locators import HomeLocators
from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    driver = None

    def authentication_user(self):
        self.get_url(Constants.URL_LOGIN)
        self.set_text_to_element(LoginLocators.EMAIL_FIELD, LoginLocators.EMAIL)
        self.set_text_to_element(LoginLocators.PASSWORD_FIELD, LoginLocators.PASSWORD)
        self.click_on_element_without_wait(LoginLocators.ENTER_BUTTON)
        self.wait_element(HomeLocators.ENTER_BUTTON)


