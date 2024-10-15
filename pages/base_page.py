import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    url = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход к {url}')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('ожидание элемента {locator}')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
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

    @allure.step('Получение текста элемента {locator}')
    def get_count_elements(self, locator):
        cnt=self.driver.find_elements(*locator)
        return len(cnt)

    @allure.step('Переход в конец страницы')
    def scroll_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

