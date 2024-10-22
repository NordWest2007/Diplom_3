import allure

from constants import Constants
from locators.home_locators import HomeLocators
from locators.account_locators import AccountLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    driver = None

    @allure.step('Клик на Личный кабинет')
    def click_account(self):
        self.wait_element(HomeLocators.ACCOUNT_BUTTON).click()

    @allure.step('Ожидание кнопки Сохранить')
    def wait_save_button(self):
        self.wait_element(AccountLocators.SAVE_BUTTON)

    @allure.step('Клик на Историю заказов')
    def wait_history_button(self):
        self.wait_element(AccountLocators.HISTORY_BUTTON).click()

    @allure.step('Ожидание заголовка Вход')
    def wait_enter_button(self):
        self.wait_element(AccountLocators.ENTER_TEXT)

    @allure.step('Клик на Выход из аккаунта')
    def wait_exit_button(self):
        self.wait_element(AccountLocators.EXIT_BUTTON).click()

    @allure.step('Переход на страницу Забыли пароль')
    def click_forgot_link(self):
        self.get_url(Constants.URL_LOGIN)
        self.click_on_element(AccountLocators.FORGOT_LINK)

    @allure.step('Ввести пароль')
    def set_password(self):
        self.set_text_to_element(AccountLocators.PASSWORD_FIELD, Constants.PASSWORD)

    @allure.step('Клик на Посмотреть пароль')
    def click_password_view(self):
        self.wait_element(AccountLocators.PASSWORD_VIEW).click()

    @allure.step('Элемент видимый пароль')
    def password_visible(self):
        return self.wait_element(AccountLocators.PASSWORD_VIEW_FIELD)

    @allure.step('Перейти на странице логина')
    def get_login_url(self):
        self.get_url(Constants.URL_LOGIN)

    @allure.step('Авторизация ')
    def authentication_user(self,email, password):
        self.get_url(Constants.URL_LOGIN)
        self.set_text_to_element(AccountLocators.EMAIL_FIELD, email)
        self.set_text_to_element(AccountLocators.PASSWORD_FIELD, password)
        self.click_on_element_without_wait(AccountLocators.ENTER_BUTTON)
        self.wait_element(HomeLocators.ENTER_BUTTON)
