from selenium.webdriver.common.by import By


class HomeLocators:
    ENTER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    FEED_BUTTON = (By.XPATH, '//a[@href="/feed"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::*')
    ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]")
    MODAL_WINDOW_CLOSE_INGREDIENT = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    MODAL_WINDOW_CLOSE_ORDER = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    BUNS = (By.XPATH, '//div[contains(@class,"BurgerIngredients_ingredients")]/ul[1]/a')
    SAUCES = (By.XPATH, '//div[contains(@class,"BurgerIngredients_ingredients")]/ul[2]/a')
    INGREDIENTS = (By.XPATH, '//div[contains(@class,"BurgerIngredients_ingredients")]/ul[3]/a')
    MODAL_WINDOW_INVISIBILITY = (By.XPATH, "//section[contains(@class,'Modal_modal')]")

    BURGER_MAKE = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]")
    COUNTER = (By.XPATH, '//div[contains(@class,"BurgerIngredients_ingredients")]/ul[3]/a[{}]/div[contains(@class,'
                         '"counter_counter")]/p')
    CREATE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER=(By.XPATH,'//h2[contains(@class,"Modal_modal__title_shadow")]')


