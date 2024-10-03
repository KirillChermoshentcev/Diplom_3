from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    RECOVER_PASSWORD_LINK = (By.XPATH, '//a[contains(text(),"Восстановить пароль")]')
    EMAIL_INPUT = (By.XPATH, '//input[contains(@class, "input__textfield")]')
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    PASSWORD_INPUT = (By.XPATH, '//input[contains(@type, "password")]')
    HIDE_PASSWORD = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')

    PASSWORD_VISABILITY_ACTIVE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                            '"input_status_active")]')

    PASSWORD_VISABILITY_NOT_ACTIVE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                      '"input_type_password")]')

