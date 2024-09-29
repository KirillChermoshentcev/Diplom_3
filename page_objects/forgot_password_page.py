import allure
from page_objects.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from data import UserData


class ForgotPasswordPage(BasePage):

    @allure.step('Переход на страницу восстановления пароля')
    def go_to_recovery_password_page(self):
        self.wait_visibility_of_element(ForgotPasswordPageLocators.RECOVER_PASSWORD_LINK)
        self.click_on_element(ForgotPasswordPageLocators.RECOVER_PASSWORD_LINK)

    @allure.step('Проверка отображения поля для ввода email')
    def check_email_input_is_displaying(self):
        return self.check_element_is_displaying(ForgotPasswordPageLocators.EMAIL_INPUT)

    @allure.step('Ввод email')
    def send_email_in_input(self):
        self.wait_visibility_of_element(ForgotPasswordPageLocators.EMAIL_INPUT)
        email = UserData.EMAIL
        self.send_keys_to_input(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step('Клик на ссылку восстановления пароля')
    def click_on_recover_button(self):
        self.wait_visibility_of_element(ForgotPasswordPageLocators.RECOVER_BUTTON)
        self.click_on_element(ForgotPasswordPageLocators.RECOVER_BUTTON)

    @allure.step('Проверка отображения поля для ввода пароля')
    def check_password_input_is_displaying(self):
        self.wait_visibility_of_element(ForgotPasswordPageLocators.PASSWORD_INPUT)
        return self.check_element_is_displaying(ForgotPasswordPageLocators.PASSWORD_INPUT)

    @allure.step('Ввод пароля')
    def send_password_in_input(self):
        self.wait_visibility_of_element(ForgotPasswordPageLocators.PASSWORD_INPUT)
        password = UserData.PASSWORD
        self.send_keys_to_input(ForgotPasswordPageLocators.PASSWORD_INPUT, password)

    @allure.step('Клик на иконку скрытия пароля')
    def click_on_hide_password_icon(self):
        self.wait_visibility_of_element(ForgotPasswordPageLocators.HIDE_PASSWORD)
        self.click_on_element(ForgotPasswordPageLocators.HIDE_PASSWORD)

    @allure.step('Проверка, что поле с паролем активно')
    def check_password_field_is_visible(self):
        return self.check_element_is_displaying(ForgotPasswordPageLocators.PASSWORD_VISABILITY_ACTIVE)

    @allure.step('Проверка, что поле с паролем неактивно')
    def check_password_field_is_not_visible(self):
        return self.check_element_is_displaying(ForgotPasswordPageLocators.PASSWORD_VISABILITY_NOT_ACTIVE)


