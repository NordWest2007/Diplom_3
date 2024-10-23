import allure


from data.data_url import DataUrl
from pages.account_page import AccountPage
from pages.forgot_password_page import ForgotPasswordPage


@allure.feature("Восстановление пароля")
@allure.suite("Восстановление пароля")
class TestForgotPassword:
    @allure.sub_suite("клик Восстановить пароль")
    @allure.title("переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_click_forgot_password(self, driver):
        account = AccountPage(driver)
        account.click_forgot_link()
        forgot = ForgotPasswordPage(driver)
        forgot.check_url(DataUrl.URL_FORGOT_PASSWORD)

    @allure.sub_suite("Отправка на почту")
    @allure.title("ввод почты и клик по кнопке «Восстановить»")
    def test_input_email(self, driver):
        account = AccountPage(driver)
        account.click_forgot_link()
        forgot = ForgotPasswordPage(driver)
        forgot.set_email()
        forgot.click_restore_button()
        account.wait_save_button()
        forgot.check_url(DataUrl.URL_RESET_PASSWORD)
