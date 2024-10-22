import allure
import pytest
import requests

from selenium import webdriver

from constants import Constants
from data_for_api import PAYLOAD_FOR_USER
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
        requests.post(Constants.ENDPOINT_CREATE_USER, data=PAYLOAD_FOR_USER)

    yield PAYLOAD_FOR_USER['email'], PAYLOAD_FOR_USER['password']

    with allure.step('Удаление регистрации пользователя'):
        response = requests.post(Constants.ENDPOINT_LOGIN, data=PAYLOAD_FOR_USER)
        token = response.json()['accessToken'].split(' ')[1]
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(token)}
        response = requests.delete(Constants.ENDPOINT_DELETE, headers=headers)



@allure.step("Авторизация")
@pytest.fixture()
def authentication_user(driver, create_user_api):
    account = AccountPage(driver)
    account.authentication_user(create_user_api[0], create_user_api[1])


@allure.step('Создание заказа')
@pytest.fixture()
def create_order(driver):
    home = HomePage(driver)
    return home.create_order()
