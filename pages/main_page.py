import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Нажать на логотип Яндекса")
    def click_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Нажать на Самокат в логотипе")
    def click_scooter(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на кнопку Заказать в хедере")
    def click_header_order(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_HEAD)

    @allure.step("Нажать на кнопку Заказать в центре")
    def click_footer_order(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_MID)

    @allure.step("Открыть вопрос из списка")
    def click_question(self, question_number):
        number_locator = (MainPageLocators.question_number(question_number))
        self.wait_for_element(number_locator)
        self.scroll_to_element(number_locator)
        self.click_on_element(number_locator)

    @allure.step("Сравнить текст в вопросе")
    def check_question_text(self, number, expected_text):
        actual_text = self.get_text(MainPageLocators.question_answer(number))
        assert actual_text == expected_text

    @allure.step("Закрыть попап с куки")
    def close_cookies_popup(self):
        try:
            self.wait_for_element(MainPageLocators.COCKIE_BUTTON)
            self.click_on_element(MainPageLocators.COCKIE_BUTTON)
        except (TimeoutException, NoSuchElementException):
            print("Куки не появились")

    @allure.step("Дождаться появления логотипа Дзена")
    def wait_for_dzen_logo(self):
        self.wait_for_element(MainPageLocators.DZEN_LOGO)



