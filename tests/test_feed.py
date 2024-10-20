import allure

from constants import Constants
from locators.feed_locators import FeedLocators
from locators.home_locators import HomeLocators
from locators.profile_locators import ProfileLocators
from pages.feed_page import FeedPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.feature("Лента заказов")
@allure.suite("Лента заказов")
class TestFeed:

    @allure.sub_suite("Клик на заказ")
    @allure.title("если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order(self, driver):
        feed = FeedPage(driver)
        feed.get_url(Constants.URL_FEED)
        feed.wait_element(FeedLocators.ORDER).click()
        assert feed.wait_element(FeedLocators.MODAL_ORDER_WINDOW)
        assert feed.get_data_history_order() == feed.get_data_detail_order()

    @allure.sub_suite("Заказы в ленте")
    @allure.title("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_customer_orders_in_list_orders(self, driver, authentication_user):
        list_custom_order = []
        list_all_order = []
        feed = FeedPage(driver)
        feed.get_url(Constants.URL_HOME)
        feed.wait_element(HomeLocators.ACCOUNT_BUTTON)
        feed.click_on_element(HomeLocators.ACCOUNT_BUTTON)
        feed.click_on_element(ProfileLocators.HISTORY_BUTTON)

        custom_orders = feed.wait_elements(ProfileLocators.ORDER_LIST)
        for order in custom_orders:
            list_custom_order.append(order.text)
        feed.get_url(Constants.URL_FEED)
        all_orders = feed.wait_elements(FeedLocators.ORDERS)
        for order in all_orders:
            list_all_order.append(order.text)

        for order in list_custom_order:
            assert order in list_custom_order

    @allure.sub_suite("Счетчики")
    @allure.title("при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_create_new_order_increment_counter(self, driver, authentication_user):

        feed = FeedPage(driver)
        feed.get_url(Constants.URL_FEED)
        feed.wait_element(FeedLocators.COUNTER_ALL)
        cnt = int(feed.get_text_from_element(FeedLocators.COUNTER_ALL))

        feed.get_url(Constants.URL_HOME)
        home = HomePage(driver)
        home.create_order()
        home.click_on_element(HomeLocators.CREATE_ORDER)

        feed.get_url(Constants.URL_FEED)
        feed.wait_element(FeedLocators.COUNTER_ALL)
        assert cnt < int(feed.get_text_from_element(FeedLocators.COUNTER_ALL))

    @allure.sub_suite("Счетчики")
    @allure.title("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_create_new_order_increment_day_counter(self, driver, authentication_user):

        feed = FeedPage(driver)
        feed.get_url(Constants.URL_FEED)
        feed.wait_element(FeedLocators.COUNTER_DAY)
        number = int(feed.get_text_from_element(FeedLocators.COUNTER_DAY))

        feed.get_url(Constants.URL_HOME)
        home = HomePage(driver)
        home.create_order()
        home.click_on_element(HomeLocators.CREATE_ORDER)

        feed.get_url(Constants.URL_FEED)
        feed.wait_element(FeedLocators.COUNTER_DAY)
        assert number < int(feed.get_text_from_element(FeedLocators.COUNTER_DAY))

    @allure.sub_suite("В работе")
    @allure.title("после оформления заказа его номер появляется в разделе В работе")
    def test_new_order_at_work(self, driver, authentication_user):

        home = HomePage(driver)
        home.get_url(Constants.URL_HOME)
        home.create_order()
        home.click_on_element(HomeLocators.CREATE_ORDER)
        order_number = '9999'
        while order_number == '9999':
            order_number = home.get_text_from_element(HomeLocators.ORDER_NUMBER)

        home.get_url(Constants.URL_FEED)
        orders_at_work = home.wait_elements(FeedLocators.ALL_ORDER_AT_WORK)
        if len(orders_at_work) == 1:
            while orders_at_work[0].text == 'Все текущие заказы готовы!':
                orders_at_work = home.wait_elements(FeedLocators.ALL_ORDER_AT_WORK)
        assert order_number in orders_at_work[0].text
