import random

import allure
from selenium.webdriver import ActionChains
from constants import Constants
from locators.home_locators import HomeLocators
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.feature("Основной функционал")
@allure.suite("Основной функционал")
class TestHome:
    @allure.sub_suite("Переходы")
    @allure.title("на «Конструктор»")
    def test_click_constructor(self, driver):
        home = HomePage(driver)
        home.get_url(Constants.URL_LOGIN)
        home.click_on_element(HomeLocators.CONSTRUCTOR_BUTTON)
        assert driver.current_url == Constants.URL_HOME

    @allure.sub_suite("Переходы")
    @allure.title("на «Лента заказов»")
    def test_click_feed(self, driver):
        home = HomePage(driver)
        home.get_url(Constants.URL_HOME)
        home.click_on_element(HomeLocators.FEED_BUTTON)
        assert driver.current_url == Constants.URL_FEED

    @allure.sub_suite("Всплывающее окно")
    @allure.title("клик на ингредиент")
    def test_click_ingredient(self, driver):
        home = HomePage(driver)
        home.get_url(Constants.URL_HOME)
        elements = home.wait_elements(HomeLocators.INGREDIENTS)
        elements[random.randint(1, len(elements) - 1)].click()

        assert home.wait_element(HomeLocators.MODAL_WINDOW)

    @allure.sub_suite("Всплывающее окно")
    @allure.title("закрывается кликом по крестику")
    def test_click_close_modal_window(self, driver):
        home = HomePage(driver)
        home.get_url(Constants.URL_HOME)
        elements = home.wait_elements(HomeLocators.INGREDIENTS)
        elements[random.randint(1, len(elements) - 1)].click()
        home.wait_element(HomeLocators.MODAL_WINDOW)
        home.wait_element(HomeLocators.MODAL_WINDOW_CLOSE_INGREDIENT).click()
        assert home.wait_element_invisibility(HomeLocators.MODAL_WINDOW_INVISIBILITY)

    @allure.sub_suite("Счетчик ингредиента")
    @allure.title("при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_drag_and_drop(self, driver):
        home = HomePage(driver)
        home.get_url(Constants.URL_HOME)
        elements = home.wait_elements(HomeLocators.INGREDIENTS)
        element_number = random.randint(1, len(elements) - 1)
        drag_from = elements[element_number]
        drag_to = home.wait_element(HomeLocators.BURGER_MAKE)
        actions = ActionChains(driver)
        for i in range(1, 3):
            actions.drag_and_drop(drag_from, drag_to)
            actions.click_and_hold()
            actions.perform()
            element = home.create_locator(HomeLocators.COUNTER, element_number + 1)
            home.wait_element(element)
            home.get_text_from_element(element)
            assert int(home.get_text_from_element(element)) == i

    @allure.sub_suite("Оформление заказа")
    @allure.title("залогиненный пользователь может оформить заказ")
    def test_create_order_for_account(self, driver):
        login = LoginPage(driver)
        login.authentication_user()
        home = HomePage(driver)
        home.get_url(Constants.URL_HOME)
        home.click_on_element(HomeLocators.CREATE_ORDER)
        assert home.wait_element(HomeLocators.MODAL_WINDOW)
