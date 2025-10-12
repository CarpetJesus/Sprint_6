from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = (By.XPATH, '//input[contains (@placeholder, "Имя")]')
    LAST_NAME_INPUT = (By.XPATH, '//input[contains (@placeholder, "Фамилия")]')
    ADDRESS_INPUT = (By.XPATH, '//input[contains (@placeholder, "Адрес")]')
    METRO_INPUT = (By.XPATH, '//input[contains (@placeholder, "метро")]')
    METRO_LIST = (By.XPATH, f'//button[@value={value}]')
    PHONE_INPUT = (By.XPATH, '//input[contains (@placeholder, "Телефон")]')
    CONTINUE_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    WHEN_INPUT = (By.XPATH, '//input[contains (@placeholder, "Когда")]')
    ORDER_DATE_FORM = (By.CSS_SELECTOR, '.Dropdown-control')
    ORDER_DATE = (By.XPATH, f'//div[text()={date}]')
    VEHICLE_COLOR = (By.XPATH, f'//input[@id={color}]')
    COMMENT_INPUT = (By.XPATH, '//input[contains (@placeholder, "Комментарий")]')
    ORDER_FORM_BUTTON = (By.XPATH, "//div[contains(@class, 'Order')]//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//div[contains(@class, 'Order')]//button[text()='Да']")
    CONFIRM_WINDOW = (By.XPATH, "//div[text()='Заказ оформлен']")
    ORDER_PAGE_DATA_NAME = (By.XPATH, '//div[text()="Имя"]/following-sibling::div')



