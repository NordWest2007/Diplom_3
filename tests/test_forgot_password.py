import allure

from constants import Constants
from pages.forgot_password_page import ForgotPasswordPage


@allure.feature("Восстановление пароля")
@allure.suite("Восстановление пароля")
class TestForgotPassword:
    @allure.sub_suite("клик Восстановить пароль")
    @allure.title("переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_click_forgot_password(self, driver):
        forgot = ForgotPasswordPage(driver)
        forgot.click_forgot_link()
        forgot.check_url(Constants.URL_FORGOT_PASSWORD)

    @allure.sub_suite("Отправка на почту")
    @allure.title("ввод почты и клик по кнопке «Восстановить»")
    def test_input_email(self, driver):
        forgot = ForgotPasswordPage(driver)
        forgot.click_forgot_link()
        forgot.set_email()
        forgot.click_restore_button()
        forgot.wait_save_button()
        forgot.check_url(Constants.URL_RESET_PASSWORD)
