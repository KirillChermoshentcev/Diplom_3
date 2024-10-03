from locators.order_history_page_locators import OrderHistoryPageLocators
from page_objects.base_page import BasePage
import allure


class OrderHistoryPage(BasePage):

    @allure.step('Ожидание видимости секции с заказами')
    def wait_visibility_of_order_section(self):
        self.wait_visibility_of_element(OrderHistoryPageLocators.ORDER_LIST_SECTION)

    @allure.step('Получение номера заказа в карточке заказа')
    def get_order_card_id(self):
        return self.get_text_from_element(OrderHistoryPageLocators.ID_ORDER_CARD)