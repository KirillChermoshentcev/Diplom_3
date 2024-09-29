from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:

    TITLE_OF_ORDERS_FEED_PAGE = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')

    ORDER_CARD_IN_FEED = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')

    MODAL_OF_ORDER_DETAILS = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
                                        '//div[contains(@class, "Modal_orderBox")]')

    TITLE_OF_MODAL_ORDER_DETAILS = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
                                              '//div[contains(@class, "Modal_orderBox")]//h2')

    QUANTITY_COMPLETE_ORDERS_FOR_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')

    QUANTITY_COMPLETE_ORDERS_FOR_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]')

    NUMBER_OF_ORDER_IN_PROGRESS_SECTION = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]'
                                                     '/li[contains(@class, "text_type_digits-default")]')

    ORDER_ID_IN_FEED = (By.XPATH, './/*[text()="{order_id}"]')
