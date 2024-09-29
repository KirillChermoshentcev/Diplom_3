from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент на странице')
    def find_element_with_wait(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(locator)

    @allure.step('Ожидание прогрузки элемента')
    def wait_visibility_of_element(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_until_element_is_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step('Проверка отображения элемента')
    def check_element_is_displaying(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Проверка, что элемент кликабелен')
    def check_element_is_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Клик на элемент')
    def click_on_element(self, locator):
        element = self.check_element_is_clickable(locator)
        action_click = ActionChains(self.driver)
        action_click.move_to_element(element).click().perform()

    @allure.step('Ожидание смены текста элемента')
    def waiting_for_element_text_is_change(self, locator, value, timeout=15):
        WebDriverWait(self.driver, timeout).until_not(EC.text_to_be_present_in_element(locator, value))

    @allure.step('Получение текста на элементе')
    def get_text_from_element(self, locator):
        WebDriverWait(self.driver, timeout=15).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    @allure.step('Ввод символов в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Ожидание закрытия элемента')
    def wait_of_closing_element(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator))

    @allure.step('Получение текущего url')
    def get_current_url(self):
        return self.driver.current_url



