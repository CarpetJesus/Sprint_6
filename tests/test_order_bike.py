import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from curl import *
from data import FormData


class TestOrderBike:
    @allure.title("Тест заполения формы заказа самоката")
    @pytest.mark.parametrize(
        "button, name, last_name, address, station_name, phone, delivery_date, period, color, comment", FormData.test_data
    )
    def test_order_bike_with_correct_data(
        self, driver, button, name, last_name, address, station_name, phone, delivery_date, period, color, comment
    ):
        order_page = OrderPage(driver)
        order_page.close_cookies_popup()
        order_page.click_on_element(button)

        order_page.check_current_url(order_site)

        order_page.fill_order_data(
            name, last_name, address, station_name, phone, delivery_date, period, color, comment
        )

        order_page.click_order_button()
        order_page.click_confirm_order_button()

        order_page.check_is_window_visible()

    @allure.title('Проверка перехода на главную страницу после нажатия на кнопку "Самокат" в хэдере')
    def test_click_on_bike_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_header_order()

        main_page.check_current_url(order_site)

        main_page.click_scooter()

        main_page.check_current_url(main_site)





