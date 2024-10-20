from selenium.webdriver.common.by import By


class ProfileLocators:
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    ORDER_LAST = (By.XPATH, '//li[contains(@class,"OrderHistory_listItem")][last()]//div[contains(@class,'
                            '"OrderHistory_textBox")]/p[contains(@class,"text text_type_digits-default")]')
