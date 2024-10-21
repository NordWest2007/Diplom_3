import random

import allure
from selenium.webdriver import ActionChains

from constants import Constants
from locators.home_locators import HomeLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    driver = None

    @allure.step('Переход к домашней странице')
    def get_url_home(self):
        self.get_url(Constants.URL_HOME)

    @allure.step('Клик на Конструктор')
    def click_constructor(self):
        self.click_on_element(HomeLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик Лента Заказов')
    def click_feed(self):
        self.click_on_element(HomeLocators.FEED_BUTTON)

    @allure.step('Клик на случайном Ингредиенте')
    def click_on_random_ingredient(self):
        elements = self.wait_elements(HomeLocators.INGREDIENTS)
        elements[random.randint(1, len(elements) - 1)].click()

    @allure.step('Ожидание модального окна')
    def wait_modal_window(self):
        return self.wait_element(HomeLocators.MODAL_WINDOW)

    @allure.step('Закрытие модального окна с информацией об ингредиенте')
    def click_close_modal_window(self):
        self.wait_element(HomeLocators.MODAL_WINDOW_CLOSE_INGREDIENT).click()

    @allure.step('Модальное окно невидимое')
    def modal_window_invisible(self):
        return self.wait_element_invisibility(HomeLocators.MODAL_WINDOW_INVISIBILITY)

    @allure.step('Получение списка ингредиентов')
    def get_ingredients(self):
        return self.wait_elements(HomeLocators.INGREDIENTS)

    @allure.step('Элемент Бургер')
    def element_burger(self):
        return self.wait_element(HomeLocators.BURGER_MAKE)

    @allure.step('Счетчик у выбранного ингредиента')
    def get_counter_locator(self, element_number):
        return self.create_locator(HomeLocators.COUNTER, element_number + 1)

    @allure.step('Переход к странице логина')
    def get_url_login(self):
        self.get_url(Constants.URL_LOGIN)

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        order_number = '9999'
        while order_number == '9999':
            order_number = self.get_text_from_element(HomeLocators.ORDER_NUMBER)
        return order_number

    @allure.step('Создание заказа')
    def create_order(self) -> None:
        self.get_url(Constants.URL_HOME)
        buns = self.wait_elements(HomeLocators.BUNS)
        element_number = random.randint(1, len(buns) - 1)
        drag_from = buns[element_number]
        drag_to = self.wait_element(HomeLocators.BURGER_MAKE)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag_from, drag_to).click_and_hold().perform()

        ingredients = self.wait_elements(HomeLocators.INGREDIENTS)
        element_number = random.randint(1, len(ingredients) - 1)
        drag_from = ingredients[element_number]
        drag_to = self.wait_element(HomeLocators.BURGER_MAKE)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag_from, drag_to).click_and_hold().perform()

        sauces = self.wait_elements(HomeLocators.SAUCES)
        element_number = random.randint(1, len(sauces) - 1)
        drag_from = sauces[element_number]
        drag_to = self.wait_element(HomeLocators.BURGER_MAKE)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag_from, drag_to).click_and_hold().perform()
        self.click_on_element(HomeLocators.CREATE_ORDER)
        order_number = f"0{self.get_order_number()}"
        return order_number
