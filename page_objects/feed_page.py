from page_objects.base_page import BasePage
from locators.feed_page_locators import OrdersFeedPageLocators
import allure


class FeedPage(BasePage):

    @allure.step('Получение заголовка страницы заказов')
    def get_title_text_of_feed_page(self):
        return self.get_text_from_element(OrdersFeedPageLocators.TITLE_OF_ORDERS_FEED_PAGE)

    @allure.step('Проверка отображения окна с деталями заказа ')
    def check_modal_order_details_is_displayed(self):
        self.wait_visibility_of_element(OrdersFeedPageLocators.MODAL_OF_ORDER_DETAILS)
        return self.check_element_is_displaying(OrdersFeedPageLocators.MODAL_OF_ORDER_DETAILS)

    @allure.step('Клик на карточку заказа')
    def click_on_order_card(self):
        self.wait_visibility_of_element(OrdersFeedPageLocators.ORDER_CARD_IN_FEED)
        self.click_on_element(OrdersFeedPageLocators.ORDER_CARD_IN_FEED)

    @allure.step('Получение заголовка окна с деталями заказа')
    def get_title_text_of_modal_order_details(self):
        return self.get_text_from_element(OrdersFeedPageLocators.TITLE_OF_MODAL_ORDER_DETAILS)

    @allure.step('Проверка отображения номера заказа в ленте заказов')
    def check_id_order_is_displayed_in_feed(self, order_id):
        locator = (OrdersFeedPageLocators.ORDER_CARD_IN_FEED[0],
                   OrdersFeedPageLocators.ORDER_ID_IN_FEED[1].format(order_id=order_id))
        element = self.wait_visibility_of_element(locator)
        return self.check_element_is_displaying(locator)

    @allure.step('Получение количества заказов, выполненных за все время')
    def get_quantity_orders_for_all_time(self):
        self.wait_visibility_of_element(OrdersFeedPageLocators.QUANTITY_COMPLETE_ORDERS_FOR_ALL_TIME)
        return self.get_text_from_element(OrdersFeedPageLocators.QUANTITY_COMPLETE_ORDERS_FOR_ALL_TIME)

    @allure.step('Получение количества заказов, выполненных за сегодня')
    def get_quantity_orders_for_today(self):
        self.wait_visibility_of_element(OrdersFeedPageLocators.QUANTITY_COMPLETE_ORDERS_FOR_TODAY)
        return self.get_text_from_element(OrdersFeedPageLocators.QUANTITY_COMPLETE_ORDERS_FOR_TODAY)

    @allure.step('Получение последнего заказа, который взяли в работу')
    def get_number_of_order_in_progress_section(self):
        return self.get_text_from_element(OrdersFeedPageLocators.NUMBER_OF_ORDER_IN_PROGRESS_SECTION)

