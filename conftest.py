import allure
import pytest
from selenium import webdriver

from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.step("Тест запускается в {params}")
@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    driver = None
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    elif request.param == 'Firefox':
        driver = webdriver.Firefox()
    else:
        ValueError('driver error')
    yield driver

    driver.quit()


@allure.step("Авторизация")
@pytest.fixture()
def authentication_user(driver):
    login = LoginPage(driver)
    login.authentication_user()


@allure.step('Создание заказа')
@pytest.fixture()
def create_order(driver):
    home = HomePage(driver)
    home.create_order()
