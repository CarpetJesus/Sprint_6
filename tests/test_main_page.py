import pytest
import allure
from pages.main_page import MainPage
from curl import *
from data import Data

class TestMainPage:
    @allure.title('Проверка корректности текста вопросов')
    @pytest.mark.parametrize('question_number, item, expected_text', Data.questions)
    def test_each_question_text_valid(self, driver, question_number, item, expected_text):
        main_page = MainPage(driver)
        main_page.close_cookies_popup()

        main_page.click_question(question_number)
        main_page.check_question_text(item, expected_text)


    @allure.title('Проверка перехода на главную страницу после нажатия на кнопку "Яндекс"')
    def test_header_buttons(self, driver):
        main_page = MainPage(driver)

        main_page.click_logo()

        main_page.wait_new_page()

        main_page.switch_to_new_window()

        main_page.not_blank()

        main_page.wait_for_dzen_logo()

        main_page.check_current_url(dzen_page)




