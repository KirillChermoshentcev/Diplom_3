import allure
from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


class MainPage(BasePage):

    @allure.step('Ожидание загрузки заголовка главной страницы')
    def wait_visibility_title_of_page(self):
        self.wait_visibility_of_element(MainPageLocators.TITLE_OF_MAIN_PAGE)

    @allure.step('Получение текста заголовка главной страницы')
    def get_text_from_title_of_main_page(self):
        return self.get_text_from_element(MainPageLocators.TITLE_OF_MAIN_PAGE)

    @allure.step('Клик на кнопку "Конструктор"')
    def click_on_constructor_button(self):
        self.wait_visibility_of_element(MainPageLocators.CONSTUCTOR_BUTTON)
        self.click_on_element(MainPageLocators.CONSTUCTOR_BUTTON)

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_on_order_list_button(self):
        self.wait_visibility_of_element(MainPageLocators.ORDERS_LIST)
        self.click_on_element(MainPageLocators.ORDERS_LIST)

    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_on_personal_acc_button(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(MainPageLocators.PARSONAL_ACCOUNT_BUTTON))
        self.click_on_element(MainPageLocators.PARSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик на кнопку "Войти в аккаунт" на главной странице')
    def click_on_auth_button_main_page(self):
        self.click_on_element(MainPageLocators.AUTH_BUTTON_ACC)

    @allure.step('Клик на ингредиент')
    def click_on_ingredient(self):
        self.wait_visibility_of_element(MainPageLocators.INGREDIENT_BUN)
        self.click_on_element(MainPageLocators.INGREDIENT_BUN)

    @allure.step('Проверка, что модальное окно с деталями ингредиента отображается')
    def check_ingr_modal_window_is_displaying(self):
        self.wait_visibility_of_element(MainPageLocators.MODAL_INGR_DETAILS_HEADER)
        return self.check_element_is_displaying(MainPageLocators.MODAL_INGR_DETAILS_HEADER)

    @allure.step('Клик на кнопку закрытия модального окна деталей ингредиента')
    def click_on_close_button_in_ingr_modal_window(self):
        close_modal = self.check_element_is_clickable(MainPageLocators.MODAL_INGR_DETAILS_CLOSE_BUTTON)
        self.click_on_element(close_modal)

    @allure.step('Проверка, что модальное окно ингредиента не отображается')
    def check_ingr_modal_window_is_not_displaying(self):
        self.wait_of_closing_element(MainPageLocators.MODAL_INGR_DETAILS_HEADER)
        return not self.check_element_is_displaying(MainPageLocators.MODAL_INGR_DETAILS_HEADER)

    @allure.step('Добавление ингредиента в бургер')
    def move_ingredient_to_burger(self):
        from_element = self.check_element_is_clickable(MainPageLocators.INGREDIENT_BUN)
        to_element = self.check_element_is_clickable(MainPageLocators.INGREDIENT_CONSTRUCTION)
        action_click = ActionChains(self.driver)
        action_click.click_and_hold(from_element).move_to_element(to_element).release().perform()

    @allure.step('Получение количества ингредиента')
    def get_count_of_ingredient(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Клик на кнопку создания заказа')
    def click_on_make_order_button(self):
        self.check_element_is_clickable(MainPageLocators.MAKE_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Проверка отображения модального окна подтверждения заказа')
    def check_modal_confirmation_of_order_is_displaying(self):
        self.wait_visibility_of_element(MainPageLocators.MODAL_CONFIRM_ORDER)
        return self.check_element_is_displaying(MainPageLocators.MODAL_CONFIRM_ORDER)

    @allure.step('Получение номера заказа в окне подтверждения заказа')
    def get_number_of_order_in_confirm_modal(self):
        try:
            self.waiting_for_element_text_is_change(MainPageLocators.NUMBER_OF_ORDER_IN_MODAL, '9999')
            return self.get_text_from_element(MainPageLocators.NUMBER_OF_ORDER_IN_MODAL)
        except TimeoutException:
            print("TimeoutException: Номер заказа не прогрузился в раздел 'В работе'.")
            return None

    @allure.step('Клик на кнопку закрытия окна подтверждения заказа')
    def click_on_close_button_in_confirmation_order_modal(self):
        close_button = self.wait_until_element_is_clickable(MainPageLocators.MODAL_CONFIRM_ORDER_CLOSE_BUTTON)
        try:
            close_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", close_button)

    @allure.step('Проверка, что окно подтверждения заказа не отображается')
    def check_modal_confirmation_of_order_is_not_displaying(self):
        self.wait_of_closing_element(MainPageLocators.MODAL_CONFIRM_ORDER)
        return not self.check_element_is_displaying(MainPageLocators.MODAL_CONFIRM_ORDER)

    @staticmethod
    def get_auth_button_locator():
        # Локатор кнопки авторизации
        return MainPageLocators.AUTH_BUTTON_ACC

    @staticmethod
    def get_overlay_locator():
        # Локатор оверлея
        return MainPageLocators.OVERLAY

    def click_auth_button(self):
        # Локатор скрыт внутри метода
        self.skip_overlay(self.driver, self.get_auth_button_locator(), self.get_overlay_locator())
