import allure

from constants import Constants
from locators.forgor_password_locators import ForgotPasswordLocators
from locators.account_locators import AccountLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    driver = None

    @allure.step('Переход на страницу Забыли пароль')
    def click_forgot_link(self):
        self.get_url(Constants.URL_LOGIN)
        self.click_on_element(AccountLocators.FORGOT_LINK)

    @allure.step('внести email')
    def set_email(self):
        self.set_text_to_element(ForgotPasswordLocators.EMAIL_FIELD, Constants.EMAIL)

    @allure.step('нажать Восстановить')
    def click_restore_button(self):
        self.click_on_element_without_wait(ForgotPasswordLocators.RESTORE_BUTTON)

    @allure.step('Дождаться кнопки Сохранить')
    def wait_save_button(self):
        self.wait_element(AccountLocators.SAVE_BUTTON)
