from locators.feed_locators import FeedLocators
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