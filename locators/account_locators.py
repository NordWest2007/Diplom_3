from selenium.webdriver.common.by import By


class AccountLocators:
    FORGOT_LINK = (By.LINK_TEXT, 'Восстановить пароль')
    PASSWORD_VIEW=(By.XPATH,"//div[contains(@class,'input__icon input__icon-action')]")
    PASSWORD_FIELD=(By.XPATH,'//input[@type="password"]')
    PASSWORD_VIEW_FIELD=(By.XPATH,'//fieldset[2]//input[@type="text"]')
    EMAIL_FIELD = (By.NAME, 'name')
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ENTER_TEXT = (By.XPATH, "//h2[text()='Вход']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    ORDER_LAST = (By.XPATH, '//li[contains(@class,"OrderHistory_listItem")][last()]//div[contains(@class,'
                            '"OrderHistory_textBox")]/p[contains(@class,"text text_type_digits-default")]')