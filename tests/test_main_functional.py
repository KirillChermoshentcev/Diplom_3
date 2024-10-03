from page_objects.feed_page import FeedPage
from conftest import *
import allure


@allure.suite('Тестирование основного функционала')
class TestMainFunctional:

    @allure.title('Проверка перехода на страницу Конструктора')
    def test_go_to_constructor_page_is_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_list_button()
        main_page.click_on_constructor_button()
        assert "Соберите бургер" in main_page.get_text_from_title_of_main_page()

    @allure.title('Проверка перехода на страницу Ленты заказов')
    def test_go_to_orders_feed_page_is_success(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_on_order_list_button()
        assert feed_page.get_title_text_of_feed_page() == "Лента заказов"

    @allure.title('Проверка, что после клика на ингредиент отображается окно Деталей ингредиента')
    def test_details_modal_window_of_ingredient_is_displayed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.check_ingr_modal_window_is_displaying()

    @allure.title('Проверка закрытия окна Деталей ингредиента по клику на крестик')
    def test_closing_details_modal_window_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.click_on_close_button_in_ingr_modal_window()
        assert main_page.check_ingr_modal_window_is_not_displaying()

    @allure.title('Проверка, что счетчик количества ингредиента увеличивается после добавления в заказ')
    def test_ingredient_counter_is_increase(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_title_of_page()
        main_page.move_ingredient_to_burger()
        assert main_page.get_count_of_ingredient() == '2'

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    def test_authorized_user_can_make_order_is_success(self, driver, login_user):
        driver = login_user

        main_page = MainPage(driver)
        main_page.wait_visibility_title_of_page()
        main_page.move_ingredient_to_burger()
        main_page.click_on_make_order_button()

        assert main_page.check_modal_confirmation_of_order_is_displaying()
