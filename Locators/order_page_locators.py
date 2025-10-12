from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = (By.XPATH, '//input[contains (@placeholder, "Имя")]')
    LAST_NAME_INPUT = (By.XPATH, '//input[contains (@placeholder, "Фамилия")]')
    ADRESS_INPUT = (By.XPATH, '//input[contains (@placeholder, "Адрес")]')
    METRO_LIST = (By.XPATH, f'//button[@value={value}]')
    PHONE_INPUT = (By.XPATH, '//input[contains (@placeholder, "Телефон")]')
    CONTINUE_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    WHEN_INPUT = (By.XPATH, '//input[contains (@placeholder, "Когда")]')
    ORDER_DATE = (By.XPATH, '//div[text()="трое суток"]')
    VEHICLE_COLOR = (By.XPATH, '//input[@id="grey"]')
    ORDER_FORM_BUTTON = (By.XPATH, "//div[contains(@class, 'Order')]//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//div[contains(@class, 'Order')]//button[text()='Да']")
    CONFIRM_WINDOW = (By.XPATH, "//div[text()='Заказ оформлен']")



