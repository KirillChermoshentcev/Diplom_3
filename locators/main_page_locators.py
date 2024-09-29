from selenium.webdriver.common.by import By


class MainPageLocators:

    TITLE_OF_MAIN_PAGE = (By.XPATH, '//h1')
    PARSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')
    AUTH_BUTTON_ACC = (By.XPATH, '//button[contains(text(),"Войти в аккаунт")]')
    CONSTUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]')
    ORDERS_LIST = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')
    MAKE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    SAUCE_TAB = (By.XPATH, '//span[contains(text(),"Соусы")]')
    FILLINGS_TAB = (By.XPATH, '//span[contains(text(),"Начинки")]')
    BUNS_TAB = (By.XPATH, '//span[contains(text(),"Булки")]')
    ACTIVE_TAB = (By.XPATH, '//div[contains(@class, "tab_tab__") and contains(@class, "tab_tab_type_current__")]')

    MODAL_INGR_DETAILS_WINDOW = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]')
    MODAL_INGR_DETAILS_HEADER = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]')
    MODAL_INGR_DETAILS_CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, '
                                                 '"Modal_modal_opened")]//button[contains(@class, "close")]')
    OVERLAY = (By.XPATH, "//section[@class='Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']")

    INGREDIENT_BUN = (By.XPATH, './/*[@alt="Краторная булка N-200i"]')
    INGREDIENT_FILLING = (By.XPATH, '//a[contains(@href, "/ingredient/61c0c5a71d1f82001bdaaa70")]')
    INGREDIENT_SAUCE = (By.XPATH, '//a[contains(@href, "/ingredient/61c0c5a71d1f82001bdaaa75")]')

    INGREDIENT_CONSTRUCTION = (By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]')
    INGREDIENT_COUNTER = (By.XPATH, '//a[contains(@href, "ingredient/61c0c5a71d1f82001bdaaa6c")]'
                                    '//p[@class="counter_counter__num__3nue1"][1]')

    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[contains(text(),"История заказов")]')

    MODAL_CONFIRM_ORDER = (By.XPATH, '//div[contains(@class, "Modal_modal__container")]')
    NUMBER_OF_ORDER_IN_MODAL = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow__3ikwq")]')

    MODAL_CONFIRM_ORDER_CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
                                                  '//button[contains(@class, "close")]')

