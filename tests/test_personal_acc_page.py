import allure
from page_objects.personal_acc_page import AccountPage
from conftest import *


@allure.suite('Тестирования раздела "Личный кабинет"')
class TestPersonalAccountPage:

    @allure.title('Проверка перехода в профиль аккаунта по клику на кнопку Личный кабинет')
    def test_go_to_personal_acc_page(self, login_user, driver):
        driver = login_user

        main_page = MainPage(driver)
        main_page.wait_visibility_title_of_page()
        main_page.click_on_personal_acc_button()

        account_page = AccountPage(driver)
        account_page.wait_visibility_of_save_button()
        account_page.check_save_button_is_displaying()
        assert "account/profile" in driver.current_url

    @allure.title('Проверка перехода на вкладку История заказов')
    def test_go_to_order_history_page(self, driver, login_user):
        driver = login_user

        main_page = MainPage(driver)
        main_page.wait_visibility_title_of_page()
        main_page.click_on_personal_acc_button()

        account_page = AccountPage(driver)
        account_page.wait_visibility_of_save_button()
        account_page.check_save_button_is_displaying()
        account_page.go_to_order_history_tab()
        assert 'account/order-history' in driver.current_url

    @allure.title('Проверка выхода из аккаунта через кнопку Выход в личном кабинете')
    def test_logout(self, driver, login_user):
        driver = login_user

        main_page = MainPage(driver)
        main_page.wait_visibility_title_of_page()
        main_page.click_on_personal_acc_button()

        account_page = AccountPage(driver)
        account_page.wait_visibility_of_save_button()
        account_page.check_save_button_is_displaying()
        account_page.click_on_logout()
        assert account_page.check_enter_header_is_displayed()







