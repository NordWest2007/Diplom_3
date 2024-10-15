from selenium.webdriver.common.by import By


class LoginLocators:
    FORGOT_LINK = (By.LINK_TEXT, 'Восстановить пароль')
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_VIEW=(By.XPATH,"//div[contains(@class,'input__icon input__icon-action')]")
    PASSWORD_NOT_VIEW_FIELD=(By.XPATH,'//input[@type="password"]')
    VIEW_PASSWORD_FIELD=(By.XPATH,'//fieldset[2]//input[@type="text"]')
    NAME_FIELD = (By.NAME, 'name')
    EMAIL = 'egorova_13@gmail.com'
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")