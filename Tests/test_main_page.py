import pytest
import allure
from Pages.main_page import MainPage
from Locators.main_page_locators import MainPageLocators
from curl import *
from data import Data

class TestMainPage:
    @allure.feature('Проверка корректности текста вопросов')
    @pytest.mark.parametrize('question_number, item, expected_text', Data.questions)
    def test_each_question_text_valid(self, driver, question_number, item, expected_text):
        main_page = MainPage(driver)
        main_page.close_cookies_popup()

        main_page.click_question(question_number)
        main_page.check_question_text(item, expected_text)


    @allure.feature('Проверка перехода на главную страницу после нажатия на кнопку "Яндекс"')
    def test_header_buttons(self, driver):
        main_page = MainPage(driver)

        main_page.click_logo()

        main_page.wait_new_page()

        # переключаемся на новую вкладку
        driver.switch_to.window(driver.window_handles[1])

        main_page.not_blank()

        main_page.wait_for_element(MainPageLocators.DZEN_LOGO)

        assert driver.current_url == dzen_page



