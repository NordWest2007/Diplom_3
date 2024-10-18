from selenium.webdriver.common.by import By


class FeedLocators:
    FEED_TEXT = (By.XPATH, '//h1[text()="Лента заказов"]')
    ORDER = (By.XPATH, '//a[contains(@class,"OrderHistory_link")][1]')
    MODAL_ORDER_WINDOW = (By.XPATH, '//section[contains(@class,"Modal_modal_opened")]//div[contains(@class,'
                                    '"Modal_orderBox")]')
    COUNTER_ALL = (
    By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class,'OrderFeed_number')]")
    COUNTER_DAY = (
    By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number')]")

    ALL_ORDER_AT_WORK = (By.XPATH, '//ul[contains(@class,"OrderFeed_orderListReady")]/li')
    ORDERS = (By.XPATH, "//p[contains(@class,'text text_type_digits-default')]")
