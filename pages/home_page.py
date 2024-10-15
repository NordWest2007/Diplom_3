import allure


from pages.base_page import BasePage


class HomePage(BasePage):
    driver = None

    @allure.step('Нажатие на элемент - {locator}')
    def click_questions(self, locator):
        self.click_on_element(locator)
