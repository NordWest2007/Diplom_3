import random

import allure

from data.data_url import DataUrl
from pages.home_page import HomePage


@allure.feature("Основной функционал")
@allure.suite("Основной функционал")
class TestHome:
    @allure.sub_suite("Переходы")
    @allure.title("на «Конструктор»")
    def test_click_constructor(self, driver):
        home = HomePage(driver)
        home.get_url_home()
        home.click_constructor()
        home.check_url(DataUrl.URL_HOME)

    @allure.sub_suite("Переходы")
    @allure.title("на «Лента заказов»")
    def test_click_feed(self, driver):
        home = HomePage(driver)
        home.get_url_home()
        home.click_feed()
        home.check_url(DataUrl.URL_FEED)

    @allure.sub_suite("Всплывающее окно")
    @allure.title("клик на ингредиент")
    def test_click_ingredient(self, driver):
        home = HomePage(driver)
        home.get_url_home()
        home.click_on_random_ingredient()
        assert home.wait_modal_window()

    @allure.sub_suite("Всплывающее окно")
    @allure.title("закрывается кликом по крестику")
    def test_click_close_modal_window(self, driver):
        home = HomePage(driver)
        home.get_url_home()
        home.click_on_random_ingredient()
        home.wait_modal_window()
        home.click_close_modal_window()
        assert home.modal_window_invisible()

    @allure.sub_suite("Счетчик ингредиента")
    @allure.title("при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_drag_and_drop(self, driver):
        home = HomePage(driver)
        home.get_url_home()
        elements = home.get_ingredients()
        element_number = random.randint(1, len(elements) - 1)
        drag_from = elements[element_number]
        drag_to = home.element_burger()
        for i in range(1, 3):
            home.drag_and_drop(drag_from,drag_to)
            element = home.get_counter_locator(element_number)
            home.wait_element(element)
            assert int(home.get_text_from_element(element)) == i

    @allure.sub_suite("Оформление заказа")
    @allure.title("залогиненный пользователь может оформить заказ")
    def test_create_order_for_account(self, driver, authentication_user):
        home = HomePage(driver)
        assert home.create_order() is not None
