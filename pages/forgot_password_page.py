import allure

from constants import Constants
from locators.forgor_password_locators import ForgotPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('внести email')
    def set_email(self):
        self.set_text_to_element(ForgotPasswordLocators.EMAIL_FIELD, Constants.EMAIL)

    @allure.step('нажать Восстановить')
    def click_restore_button(self):
        self.click_on_element_without_wait(ForgotPasswordLocators.RESTORE_BUTTON)


