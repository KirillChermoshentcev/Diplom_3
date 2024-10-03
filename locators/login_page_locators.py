from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="Пароль"]')
    ENTER_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    RECOVERY_BUTTON_LINK = (By.XPATH, '//a[text()="Восстановить пароль"]')
    REGISTER_LINK = (By.XPATH, '//a[contains(text(),"Зарегистрироваться")]')
    ENTER_TITLE = (By.XPATH, '//h2[contains(text(),"Вход")]')