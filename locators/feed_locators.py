from selenium.webdriver.common.by import By


class FeedLocators:
    FORGOT_LINK = ('link','Восстановить пароль')
    QUESTION_ABOUT_MAIN = [By.XPATH, '//div[text()]="Вопросы о важном"']
    BUTTON_ORDER_FIRST = [By.XPATH, './/button[text()="Заказать" and not(contains(@class,"Button_Middle"))]']
    BUTTON_ORDER_SECOND = [By.XPATH, './/button[text()="Заказать" and (contains(@class,"Button_Middle"))]']
    BUTTON_COOKIES = [By.XPATH, '//button[contains(@class,"App_CookieButton")]']
    QUESTION_N = [By.ID, 'accordion__heading-{}']
    ANSWER_N = [By.ID, 'accordion__panel-{}']
    LOGO_SCOOTER = [By.XPATH, '//a[contains(@class,"Header_LogoScooter")]']
    LOGO_YANDEX = [By.XPATH, '//a[contains(@class,"Header_LogoYandex")]']
    DZEN = [By.XPATH, "//a[contains(@class,'dzen-layout--desktop-base-header')]"]

