import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход к {url}')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('ожидание элемента {locator}')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('ожидание элементов {locator}')
    def wait_elements(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('ожидание видимости элемента {locator}')
    def wait_element_invisibility(self, locator):
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу {locator} с предварительным ожиданием')
    def click_on_element(self, locator):
        self.wait_element(locator).click()

    @allure.step('Клик по элементу {locator}, без ожидания')
    def click_on_element_without_wait(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввод текста {set_text}  в элемент {locator}')
    def set_text_to_element(self, locator, set_text):
        self.wait_element(locator).send_keys(set_text)

    @allure.step('Получение текста элемента {locator}')
    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Создание локатора через форматирование')
    def create_locator(self, locator, num):
        return (locator[0], locator[1].format(num))

    @allure.step('Текущий URL соответствует {url}')
    def check_url(self, url):
        return self.driver.current_url == url

    @allure.step('Drag and drop')
    def drag_and_drop(self, drag_from, drag_to):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag_from, drag_to).click_and_hold().perform()
