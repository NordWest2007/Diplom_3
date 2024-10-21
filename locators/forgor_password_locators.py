from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    EMAIL_FIELD = (By.NAME, 'name')