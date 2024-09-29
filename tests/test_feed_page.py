import allure
from conftest import *
from page_objects.feed_page import FeedPage
from page_objects.order_history_page import OrderHistoryPage
from page_objects.personal_acc_page import AccountPage


@allure.suite('Тестирование раздела "Лента заказов"')
class TestFeedPage:

    @allure.title('Проверка открытия модального окна с деталями заказа после клика на карточку заказа')
    def test_modal_of_order_details_is_displayed_success(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_on_order_list_button()
        feed_page.click_on_order_card()
        assert feed_page.check_modal_order_details_is_displayed()

    @allure.title('Проверка, что созданный заказ пользователя отображается в ленте заказов')
    def test_new_order_from_history_is_displaying_in_order_feed_success(self, driver, registration_new_user_and_delete,
                                                                        create_order):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        feed_page = FeedPage(driver)
        order_history_page = OrderHistoryPage(driver)
        main_page.wait_visibility_title_of_page()
        main_page.move_ingredient_to_burger()
        main_page.click_on_make_order_button()
        main_page.check_modal_confirmation_of_order_is_displaying()
        main_page.click_on_close_button_in_confirmation_order_modal()
        main_page.check_modal_confirmation_of_order_is_not_displaying()
        main_page.click_on_personal_acc_button()
        account_page.go_to_order_history_tab()
        order_history_page.wait_visibility_of_order_section()
        id_order = order_history_page.get_order_card_id()
        main_page.click_on_order_list_button()
        assert feed_page.check_id_order_is_displayed_in_feed(id_order)

    @allure.title('Проверка, что после создания нового заказа, увеличивается счетчик общего количества'
                  'выполненных заказов')
    def test_changing_counter_of_quantity_orders_for_all_time_success(self, driver, registration_new_user_and_delete,
                                                                      create_order):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_on_order_list_button()
        order_counter_1 = feed_page.get_quantity_orders_for_all_time()
        main_page.click_on_constructor_button()
        main_page.wait_visibility_title_of_page()
        main_page.move_ingredient_to_burger()
        main_page.click_on_make_order_button()
        main_page.check_modal_confirmation_of_order_is_displaying()
        main_page.click_on_close_button_in_confirmation_order_modal()
        main_page.check_modal_confirmation_of_order_is_not_displaying()
        main_page.click_on_order_list_button()
        order_counter_2 = feed_page.get_quantity_orders_for_all_time()
        assert order_counter_2 > order_counter_1

    @allure.title('Проверка, что после создания заказа, увеличивается счетчик выполненных заказов за день ')
    def test_changing_counter_of_quantity_orders_for_today_success(self, driver, registration_new_user_and_delete,
                                                                   create_order):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_on_order_list_button()
        order_counter_1 = feed_page.get_quantity_orders_for_today()
        main_page.click_on_constructor_button()
        main_page.wait_visibility_title_of_page()
        main_page.move_ingredient_to_burger()
        main_page.click_on_make_order_button()
        main_page.check_modal_confirmation_of_order_is_displaying()
        main_page.click_on_close_button_in_confirmation_order_modal()
        main_page.check_modal_confirmation_of_order_is_not_displaying()
        main_page.click_on_order_list_button()
        order_counter_2 = feed_page.get_quantity_orders_for_today()
        assert order_counter_1 < order_counter_2

    @allure.title('Проверка отображения созданного заказа в разделе "В работе" ')
    def test_number_of_new_order_is_displaying_in_progress_section(self, driver, registration_new_user_and_delete,
                                                                   create_order):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.wait_visibility_title_of_page()
        main_page.move_ingredient_to_burger()
        main_page.click_on_make_order_button()
        main_page.check_modal_confirmation_of_order_is_displaying()
        number_of_new_order = main_page.get_number_of_order_in_confirm_modal()
        main_page.click_on_close_button_in_confirmation_order_modal()
        main_page.check_modal_confirmation_of_order_is_not_displaying()
        main_page.click_on_order_list_button()
        assert feed_page.get_number_of_order_in_progress_section() == '0'+number_of_new_order







