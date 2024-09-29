import allure
from conftest import driver
from page_objects.forgot_password_page import ForgotPasswordPage
from page_objects.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.suite('Тестирование страницы восстановления пароля')
class TestRecoveryPasswordPage:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_go_to_recovery_page_is_success(self, driver):
        main_page = MainPage(driver)
        main_page.skip_overlay(driver, MainPageLocators.AUTH_BUTTON_ACC, MainPageLocators.OVERLAY)
        recovery_password_page = ForgotPasswordPage(driver)
        recovery_password_page.go_to_recovery_password_page()
        assert 'forgot-password' in driver.current_url

    @allure.title('Проверка перехода к восстановлению пароля после ввода email и по клику на кнопку Восстановить')
    def test_click_on_recovery_button_is_success(self, driver):
        main_page = MainPage(driver)
        main_page.skip_overlay(driver, MainPageLocators.AUTH_BUTTON_ACC, MainPageLocators.OVERLAY)
        recovery_password_page = ForgotPasswordPage(driver)
        recovery_password_page.go_to_recovery_password_page()
        recovery_password_page.send_email_in_input()
        recovery_password_page.click_on_recover_button()
        assert recovery_password_page.check_password_input_is_displaying()

    @allure.title('Проверка отображения пароля после клика на иконку "показать"(глаз) в инпуте')
    def test_activate_visibility_of_password_is_success(self, driver):
        main_page = MainPage(driver)
        main_page.skip_overlay(driver, MainPageLocators.AUTH_BUTTON_ACC, MainPageLocators.OVERLAY)
        recovery_password_page = ForgotPasswordPage(driver)
        recovery_password_page.go_to_recovery_password_page()
        recovery_password_page.send_email_in_input()
        recovery_password_page.click_on_recover_button()
        recovery_password_page.send_password_in_input()
        recovery_password_page.click_on_hide_password_icon()
        assert recovery_password_page.check_password_field_is_visible()

    @allure.title('Проверка, что после повторного клика на иконку "показать"(глаз) пароль скрывается')
    def test_deactivate_visibility_of_password_is_success(self, driver):
        main_page = MainPage(driver)
        main_page.skip_overlay(driver, MainPageLocators.AUTH_BUTTON_ACC, MainPageLocators.OVERLAY)
        recovery_password_page = ForgotPasswordPage(driver)
        recovery_password_page.go_to_recovery_password_page()
        recovery_password_page.send_email_in_input()
        recovery_password_page.click_on_recover_button()
        recovery_password_page.send_password_in_input()
        recovery_password_page.click_on_hide_password_icon()
        recovery_password_page.click_on_hide_password_icon()
        assert recovery_password_page.check_password_field_is_not_visible()




