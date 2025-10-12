import pytest
import allure
from Pages.order_page import OrderPage
from Pages.main_page import MainPage
from curl import *
from data import FormData


class TestOrderBike:
    @allure.feature("Тест заполения формы заказа самоката")
    @pytest.mark.parametrize(
        "button, name, last_name, address, station_name, phone, delivery_date, period, color, comment", FormData.test_data
    )
    def test_order_bike_with_correct_data(
            self, driver, button, name, last_name, address, station_name, phone, delivery_date, period, color, comment
    ):
        main_page = MainPage(driver)
        main_page.close_cookies_popup()
        main_page.click_on_element(button)

        assert driver.current_url == order_site

        order_page = OrderPage(driver)

        order_page.fill_order_data(
            name, last_name, address, station_name, phone, delivery_date, period, color, comment
        )

        order_page.click_order_button()
        order_page.click_confirm_order_button()

        order_page.is_confirm_window_visible()




