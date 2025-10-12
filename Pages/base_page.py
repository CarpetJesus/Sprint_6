import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Дождаться видимости элемента")
    def wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=20):
        element = wait_for_element(self, locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Клик по элементу")
    def click_on_element(self, locator, timeout=20):
        element = wait_for_element(self, locator, timeout)
        element.click()

    @allure.step("Ввод текста в поле")
    def enter_text(self, locator, text, timeout=20):
        element = wait_for_element(self, locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator, timeout=20):
        element = wait_for_element(self, locator, timeout)
        return element.text

    @allure.step("Проверить что атрибут элемента содержит текст")
    def check_attribute_contains_text(self, locator, attribute, text, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, text)
        )

