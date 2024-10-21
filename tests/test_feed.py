import allure
from pages.feed_page import FeedPage


@allure.feature("Лента заказов")
@allure.suite("Лента заказов")
class TestFeed:

    @allure.sub_suite("Клик на заказ")
    @allure.title("если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order(self, driver):
        feed = FeedPage(driver)
        feed.get_feed_url()
        feed.click_order()
        assert feed.open_order_window()
        assert feed.get_data_history_order() == feed.get_data_detail_order()

    @allure.sub_suite("Заказы в ленте")
    @allure.title("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_customer_orders_in_list_orders(self, driver, authentication_user, create_order):
        feed = FeedPage(driver)
        feed.go_to_history()
        last_customer_order = feed.get_customer_order()
        feed.get_feed_url()
        list_all_order = feed.get_all_order()
        assert last_customer_order in list_all_order

    @allure.sub_suite("Счетчики")
    @allure.title("при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_create_new_order_increment_counter(self, driver, authentication_user):
        feed = FeedPage(driver)
        cnt = feed.get_counter_all_order()
        feed.create_order(driver)
        feed.get_feed_url()

        assert cnt < feed.get_counter_all_orders()

    @allure.sub_suite("Счетчики")
    @allure.title("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_create_new_order_increment_day_counter(self, driver, authentication_user):
        feed = FeedPage(driver)
        feed.get_feed_url()
        number = feed.get_counter_day_order()
        feed.create_order(driver)
        feed.get_feed_url()

        assert number < feed.get_counter_day_order()

    @allure.sub_suite("В работе")
    @allure.title("после оформления заказа его номер появляется в разделе В работе")
    def test_new_order_at_work(self, driver, authentication_user, create_order):
        feed = FeedPage(driver)
        order_number = create_order
        feed.get_feed_url()
        orders_at_work = feed.get_order_at_work()

        assert order_number in orders_at_work
