from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:

    ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
    TITLE_ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')
    ID_ORDER_CARD = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]')
    ORDER_LIST_SECTION = (By.XPATH, '//div[contains(@class, "OrderHistory_orderHistory__")]')