from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = (By.XPATH, '//input[contains (@placeholder, "Имя")]')
    LAST_NAME_INPUT = (By.XPATH, '//input[contains (@placeholder, "Фамилия")]')
    ADDRESS_INPUT = (By.XPATH, '//input[contains (@placeholder, "Адрес")]')
    METRO_INPUT = (By.XPATH, '//input[contains (@placeholder, "метро")]')
    METRO_FORM_LIST = (By.CLASS_NAME, "select-search__options")
    PHONE_INPUT = (By.XPATH, '//input[contains (@placeholder, "Телефон")]')
    CONTINUE_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    WHEN_INPUT = (By.XPATH, '//input[contains (@placeholder, "Когда")]')
    ORDER_DATE_FORM = (By.CSS_SELECTOR, '.Dropdown-control')
    COMMENT_INPUT = (By.XPATH, '//input[contains (@placeholder, "Комментарий")]')
    ORDER_FORM_BUTTON = (By.XPATH, "//div[contains(@class, 'Order')]//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//div[contains(@class, 'Order')]//button[text()='Да']")
    CONFIRM_WINDOW = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(text(),'Заказ оформлен')]")
    ORDER_PAGE_DATA_NAME = (By.XPATH, '//div[text()="Имя"]/following-sibling::div')
    COCKIE_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']")

    @staticmethod
    def metro_list(value):
        return By.XPATH, f"//button[contains(@class, 'select-search__option')]//div[text()='{value}']"

    @staticmethod
    def order_date(date):
        return By.XPATH, f'//div[contains(@class, "Dropdown-option") and text()="{date}"]'

    @staticmethod
    def vehicle_color(color):
        return By.XPATH, f'//input[@id="{color}"]'

    @staticmethod
    def calendar_date(day):
        return By.XPATH, f'//div[contains(@class,"react-datepicker__day") and @aria-label="{day}"]'




