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

    MODAL_DETAILS_NUMBER_ORDER = (By.XPATH, '//section[contains(@class,"Modal_modal_opened")]//p[contains(@class,'
                                            '"text_type_digits-default")]')
    MODAL_DETAILS_NUMBER_NAME = (By.XPATH, '//section[contains(@class,"Modal_modal_opened")]//div[contains(@class,'
                                           '"Modal_modal__contentBox")]//h2')
    MODAL_DETAILS_BURGER_PRICE = (By.XPATH, '//section[contains(@class,"Modal_modal_opened")]//div[contains(@class,'
                                            '"Modal_priceBox_")]/div/p[contains(@class,"text_type_digits-default")]')

    HISTORY_NUMBER_ORDER = (By.XPATH, '//div[contains(@class,"OrderFeed_contentBox")]/ul/li[1]//div[contains(@class,'
                                      '"OrderHistory_textBox")]/p[contains(@class,"text_type_digits-default")]')
    HISTORY_BURGER_NAME = (By.XPATH, '//div[contains(@class,"OrderFeed_contentBox")]/ul/li[1]//h2[contains(@class,'
                                     '"text_type_main-medium")]')
    HISTORY_BURGER_PRICE = (By.XPATH, '//div[contains(@class,"OrderFeed_contentBox")]/ul/li[1]//div[contains(@class,'
                                      '"OrderHistory_dataBox")]//p')
