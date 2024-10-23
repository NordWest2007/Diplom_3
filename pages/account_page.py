import allure

from constants import Constants
from data.data_url import DataUrl
from locators.account_locators import AccountLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Ожидание кнопки Сохранить')
    def wait_save_button(self):
        self.wait_element(AccountLocators.SAVE_BUTTON)

    @allure.step('Клик на Историю заказов')
    def click_history_button(self):
        self.wait_element(AccountLocators.HISTORY_BUTTON).click()

    @allure.step('Ожидание заголовка Вход')
    def wait_enter_text(self):
        self.wait_element(AccountLocators.ENTER_TEXT)

    @allure.step('Клик на Выход из аккаунта')
    def wait_exit_button(self):
        self.wait_element(AccountLocators.EXIT_BUTTON).click()

    @allure.step('Переход на страницу Забыли пароль')
    def click_forgot_link(self):
        self.get_url(DataUrl.URL_LOGIN)
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
        self.get_url(DataUrl.URL_LOGIN)

    @allure.step('Авторизация ')
    def authentication_user(self, email, password):
        self.get_url(DataUrl.URL_LOGIN)
        self.set_text_to_element(AccountLocators.EMAIL_FIELD, email)
        self.set_text_to_element(AccountLocators.PASSWORD_FIELD, password)
        self.click_on_element_without_wait(AccountLocators.ENTER_BUTTON)

    @allure.step('Получение последнего номера заказа из истории пользователя')
    def get_customer_order(self):
        custom_order = self.wait_element(AccountLocators.ORDER_LAST)
        return custom_order.text

    @allure.step('Дождаться кнопки Сохранить')
    def wait_save_button(self):
        self.wait_element(AccountLocators.SAVE_BUTTON)
