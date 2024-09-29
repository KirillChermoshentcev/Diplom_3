import allure
from page_objects.base_page import BasePage
from locators.personal_acc_page_locators import PersonalAccountPageLocators
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators


class AccountPage(BasePage):

    @allure.step('Переход на вкладку История заказов')
    def go_to_order_history_tab(self):
        self.click_on_element(PersonalAccountPageLocators.ORDER_HISTORY)

    @allure.step('Клик на кнопку Выход')
    def click_on_logout(self):
        self.click_on_element(PersonalAccountPageLocators.LOGOUT)

    @allure.step('Ожмдание отображения кнопки Сохранить')
    def wait_visibility_of_save_button(self):
        self.wait_visibility_of_element(PersonalAccountPageLocators.SAVE_BUTTON)

    @allure.step('Проверка, что кнопка Сохранить отображается')
    def check_save_button_is_displaying(self):
        return self.check_element_is_displaying(PersonalAccountPageLocators.SAVE_BUTTON)

    @allure.step('Проверка отображения заголовка Вход')
    def check_enter_header_is_displayed(self):
        return self.check_element_is_displaying(PersonalAccountPageLocators.ENTER_HEADER)

    @staticmethod  # Метод кликает по элементу с обработкой исключения и ожиданием исчезновения оверлея.
    def skip_overlay(driver, element_locator, overlay_locator=None, max_retries=5):

        wait = WebDriverWait(driver, 10)
        retries = 0

        while retries < max_retries:
            try:
                if overlay_locator:
                    wait.until(EC.invisibility_of_element_located(overlay_locator))

                element_locator = wait.until(EC.element_to_be_clickable(MainPageLocators.PARSONAL_ACCOUNT_BUTTON))
                element_locator.click()
                return
            except ElementClickInterceptedException:
                pass

                try:
                    if overlay_locator:
                        wait.until(EC.invisibility_of_element_located(overlay_locator))
                except TimeoutException:
                    print("Оверлей не исчез вовремя.")
                    raise

        raise Exception(f"Не удалось кликнуть по элементу после {max_retries} попыток.")

