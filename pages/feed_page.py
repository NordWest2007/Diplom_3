import allure


from data.data_url import DataUrl
from locators.feed_locators import FeedLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step('Клик на Оформление заказа')
    def click_order(self):
        return self.wait_element(FeedLocators.ORDER).click()

    @allure.step('Ожидание модального окна')
    def open_order_window(self):
        return self.wait_element(FeedLocators.MODAL_ORDER_WINDOW)

    @allure.step('Переход на страницу Лента заказов')
    def get_feed_url(self):
        return self.get_url(DataUrl.URL_FEED)

    @allure.step('Счетчик Всего заказов')
    def get_counter_all_orders(self):
        self.wait_element(FeedLocators.COUNTER_ALL)
        return int(self.get_text_from_element(FeedLocators.COUNTER_ALL))

    @allure.step('Счетчик Заказов за день')
    def get_counter_day_order(self):
        self.wait_element(FeedLocators.COUNTER_DAY)
        return int(self.get_text_from_element(FeedLocators.COUNTER_DAY))

    @allure.step('Получение данных из карточки')
    def get_data_history_order(self):
        history_number = self.get_text_from_element(FeedLocators.HISTORY_NUMBER_ORDER)
        history_name = self.get_text_from_element(FeedLocators.HISTORY_BURGER_NAME)
        history_price = self.get_text_from_element(FeedLocators.HISTORY_BURGER_PRICE)
        return [history_number, history_name, history_price]

    @allure.step('Получение деталей заказа')
    def get_data_detail_order(self):
        detail_number = self.get_text_from_element(FeedLocators.MODAL_DETAILS_NUMBER_ORDER)
        detail_name = self.get_text_from_element(FeedLocators.MODAL_DETAILS_NUMBER_NAME)
        detail_price = self.get_text_from_element(FeedLocators.MODAL_DETAILS_BURGER_PRICE)
        return [detail_number, detail_name, detail_price]

    @allure.step('Получение списка заказов из ленты')
    def get_all_order(self):
        list_all_order = []
        all_orders = self.wait_elements(FeedLocators.ORDERS)
        for order in all_orders:
            list_all_order.append(order.text)
        return list_all_order

    @allure.step('Получение каунтера Всего заказов')
    def get_counter_all_order(self):
        self.get_url(DataUrl.URL_FEED)
        self.wait_element(FeedLocators.COUNTER_ALL)
        cnt = int(self.get_text_from_element(FeedLocators.COUNTER_ALL))
        return cnt

    @allure.step('Ожидание заказа в Работе')
    def get_order_at_work(self):
        orders_at_work = self.wait_elements(FeedLocators.ALL_ORDER_AT_WORK)
        if len(orders_at_work) == 1:
            while orders_at_work[0].text == 'Все текущие заказы готовы!':
                orders_at_work = self.wait_elements(FeedLocators.ALL_ORDER_AT_WORK)
        return orders_at_work[0].text
