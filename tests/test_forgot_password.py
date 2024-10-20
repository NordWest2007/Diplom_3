import allure

from constants import Constants
from locators.login_locators import LoginLocators
from pages.login_page import LoginPage


@allure.feature("Восстановление пароля")
@allure.suite("Восстановление пароля")
class TestForgotPassword:
    @allure.sub_suite("клик Восстановить пароль")
    @allure.title("переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_click_forgot_password(self, driver):
        login = LoginPage(driver)
        login.get_url(Constants.URL_LOGIN)
        login.click_on_element(LoginLocators.FORGOT_LINK)
        assert driver.current_url == Constants.URL_FORGOT_PASSWORD

    @allure.sub_suite("Отправка на почту")
    @allure.title("ввод почты и клик по кнопке «Восстановить»")
    def test_input_email(self, driver):
        login = LoginPage(driver)
        login.get_url(Constants.URL_FORGOT_PASSWORD)
        login.set_text_to_element(LoginLocators.EMAIL_FIELD, LoginLocators.EMAIL)
        login.click_on_element_without_wait(LoginLocators.RESTORE_BUTTON)
        login.wait_element(LoginLocators.SAVE_BUTTON)
        assert driver.current_url == Constants.URL_RESET_PASSWORD

    @allure.sub_suite("Просмотр пароля")
    @allure.title("клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_click_view_password(self, driver):
        login = LoginPage(driver)
        login.get_url(Constants.URL_LOGIN)
        login.set_text_to_element(LoginLocators.PASSWORD_FIELD, Constants.PASSWORD)
        login.wait_element(LoginLocators.PASSWORD_VIEW).click()
        assert login.wait_element(LoginLocators.PASSWORD_VIEW_FIELD)
