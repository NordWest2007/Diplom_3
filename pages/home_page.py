import random

import allure
from selenium.webdriver import ActionChains

from constants import Constants
from locators.home_locators import HomeLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    driver = None

    @allure.step('Создание заказа')
    def create_order(self):
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

