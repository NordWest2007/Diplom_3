import allure
import pytest
from selenium import webdriver


@allure.step("Тест запускается в {params}")
#@pytest.fixture(params=['Chrome', 'Firefox'])
@pytest.fixture(params=['Chrome'])
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
