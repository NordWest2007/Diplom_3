import allure

from constants import Constants
from pages.account_page import AccountPage


@allure.feature("Личный кабинет")
@allure.suite("Личный кабинет")
class TestAccount:
    @allure.sub_suite("Переходы")
    @allure.title("переход по клику на «Личный кабинет»")
    def test_click_account_button(self, driver, authentication_user):
        account = AccountPage(driver)
        account.click_account()
        account.wait_save_button()
        account.check_url(Constants.URL_PROFILE)

    @allure.sub_suite("Переходы")
    @allure.title("переход в раздел «История заказов»")
    def test_click_history_button(self, driver, authentication_user):
        account = AccountPage(driver)
        account.click_account()
        account.wait_history_button()
        account.check_url(Constants.URL_HISTORY)

    @allure.sub_suite("Выход")
    @allure.title("выход из аккаунта")
    def test_exit_account(self, driver, authentication_user):
        account = AccountPage(driver)
        account.click_account()
        account.wait_exit_button()
        account.wait_enter_button()
        account.check_url(Constants.URL_LOGIN)

    @allure.sub_suite("Просмотр пароля")
    @allure.title("клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_click_view_password(self, driver):
        account = AccountPage(driver)
        account.get_login_url()
        account.set_password()
        account.click_password_view()
        assert account.password_visible()
