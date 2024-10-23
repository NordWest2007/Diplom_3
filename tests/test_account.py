import allure

from data.data_url import DataUrl
from pages.account_page import AccountPage
from pages.home_page import HomePage


@allure.feature("Личный кабинет")
@allure.suite("Личный кабинет")
class TestAccount:
    @allure.sub_suite("Переходы")
    @allure.title("переход по клику на «Личный кабинет»")
    def test_click_account_button(self, driver, authentication_user):
        home = HomePage(driver)
        home.click_account()
        account = AccountPage(driver)
        account.wait_save_button()
        account.check_url(DataUrl.URL_PROFILE)

    @allure.sub_suite("Переходы")
    @allure.title("переход в раздел «История заказов»")
    def test_click_history_button(self, driver, authentication_user):
        home = HomePage(driver)
        home.click_account()
        account = AccountPage(driver)
        account.click_history_button()
        account.check_url(DataUrl.URL_HISTORY)

    @allure.sub_suite("Выход")
    @allure.title("выход из аккаунта")
    def test_exit_account(self, driver, authentication_user):
        home = HomePage(driver)
        home.click_account()
        account = AccountPage(driver)
        account.wait_exit_button()
        account.wait_enter_text()
        account.check_url(DataUrl.URL_LOGIN)

    @allure.sub_suite("Просмотр пароля")
    @allure.title("клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_click_view_password(self, driver):
        account = AccountPage(driver)
        account.get_login_url()
        account.set_password()
        account.click_password_view()
        assert account.password_visible()




