from selenium.webdriver.common.by import By


class MainPageLocators:
    YANDEX_LOGO = [By.XPATH, "//img[@alt='Yandex']"]
    SCOOTER_LOGO = [By.XPATH, "//img[@alt='Scooter']"]
    ORDER_BUTTON_HEAD = [By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']"]
    ORDER_BUTTON_MID = [By.XPATH, "//div[contains(@class, 'FinishButton')]//button[text()='Заказать']"]

    @staticmethod
    def question_number(number):
        return By.XPATH, f'//div[@id="accordion__heading-{number}"]'
