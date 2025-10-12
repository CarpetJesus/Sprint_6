import pytest
import allure
from Pages.main_page import MainPage
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

