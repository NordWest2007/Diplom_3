from constants import Constants
from locators.feed_locators import FeedLocators
from locators.home_locators import HomeLocators
from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    driver = None

    def get_data_history_order(self):
        history_number = self.get_text_from_element(FeedLocators.HISTORY_NUMBER_ORDER)
        history_name = self.get_text_from_element(FeedLocators.HISTORY_BURGER_NAME)
        history_price = self.get_text_from_element(FeedLocators.HISTORY_BURGER_PRICE)
        return [history_number, history_name, history_price]

    def get_data_detail_order(self):
        detail_number = self.get_text_from_element(FeedLocators.MODAL_DETAILS_NUMBER_ORDER)
        detail_name = self.get_text_from_element(FeedLocators.MODAL_DETAILS_NUMBER_NAME)
        detail_price = self.get_text_from_element(FeedLocators.MODAL_DETAILS_BURGER_PRICE)
        return [detail_number, detail_name, detail_price]

    def get_customer_order(self):
        custom_order = self.wait_element(ProfileLocators.ORDER_LAST)
        return custom_order.text

    def get_all_order(self):
        list_all_order = []
        all_orders = self.wait_elements(FeedLocators.ORDERS)
        for order in all_orders:
            list_all_order.append(order.text)
        return list_all_order

    def get_counter_all_order(self):
        self.get_url(Constants.URL_FEED)
        self.wait_element(FeedLocators.COUNTER_ALL)
        cnt = int(self.get_text_from_element(FeedLocators.COUNTER_ALL))
        return cnt

    def get_order_number(self):
        order_number = '9999'
        while order_number == '9999':
            order_number = self.get_text_from_element(HomeLocators.ORDER_NUMBER)
        return order_number
