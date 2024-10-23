import allure
import pytest
import requests

from selenium import webdriver


from data.data_api import DataApi

from pages.home_page import HomePage
from pages.account_page import AccountPage


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


@pytest.fixture(scope='class')
def create_user_api():
    with allure.step('Регистрация пользователя'):
        requests.post(DataApi.ENDPOINT_CREATE_USER, data=DataApi.PAYLOAD_FOR_USER)

    yield DataApi.PAYLOAD_FOR_USER['email'], DataApi.PAYLOAD_FOR_USER['password']

    with allure.step('Удаление регистрации пользователя'):
        response = requests.post(DataApi.ENDPOINT_LOGIN, data=DataApi.PAYLOAD_FOR_USER)
        token = response.json()['accessToken'].split(' ')[1]
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(token)}
        requests.delete(DataApi.ENDPOINT_DELETE, headers=headers)


@allure.step("Авторизация")
@pytest.fixture()
def authentication_user(driver, create_user_api):
    account = AccountPage(driver)
    account.authentication_user(create_user_api[0], create_user_api[1])
    home = HomePage(driver)
    home.wait_enter_button()


@allure.step('Создание заказа')
@pytest.fixture()
def create_order(driver):
    home = HomePage(driver)
    return home.create_order()
