from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = (By.XPATH, '//input[contains (@placeholder, "Имя")]')
    LAST_NAME_INPUT = (By.XPATH, '//input[contains (@placeholder, "Фамилия")]')
    ADRESS_INPUT = (By.XPATH, '//input[contains (@placeholder, "Адрес")]')
    #METRO_LIST = (By.CLASS_NAME, "metro-list") Пока с этим вопросы
    PHONE_INPUT = (By.XPATH, '//input[contains (@placeholder, "Телефон")]')
    CONTINUE_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    WHEN_INPUT = (By.XPATH, '//input[contains (@placeholder, "Когда")]')


