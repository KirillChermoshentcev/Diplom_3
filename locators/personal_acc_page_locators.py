from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:

    PROFILE = (By.XPATH, '//a[contains(text(),"Профиль")]')
    ORDER_HISTORY = (By.XPATH, '//a[contains(text(),"История заказов")]')
    LOGOUT = (By.XPATH, '//button[contains(text(),"Выход")]')
    DESCRIPTION_SECTION = (By.XPATH, '//p[contains(text(),"В этом разделе вы можете изменить свои персональны")]')
    ENTER_HEADER = (By.XPATH, '//h2[contains(text(),"Вход")]')
    SAVE_BUTTON = (By.XPATH, '//button[contains(text(),"Сохранить")]')
