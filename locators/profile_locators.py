from selenium.webdriver.common.by import By


class ProfileLocators:

    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    ORDER_LIST=(By.XPATH,"//p[@class='text text_type_digits-default']")
