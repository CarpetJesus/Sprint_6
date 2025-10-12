import allure
from Locators.order_page_locators import OrderPageLocators
from Pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Выбрать станию метро")
    def select_metro_station(self, station_name):
        self.click_on_element(OrderPageLocators.METRO_INPUT)
        self.wait_for_element(OrderPageLocators.METRO_FORM_LIST)
        station = OrderPageLocators.metro_list(station_name)
        self.scroll_to_element(station)
        self.click_on_element(station)

    @allure.step("Нажать на кнопку Далее")
    def click_next_button(self):
        self.scroll_to_element(OrderPageLocators.CONTINUE_BUTTON)
        self.click_on_element(OrderPageLocators.CONTINUE_BUTTON)

    @allure.step("Выбрать срок аренды")
    def select_rent_period(self, period):
        self.click_on_element(OrderPageLocators.ORDER_DATE_FORM)
        date_locator = OrderPageLocators.order_date(period)
        self.scroll_to_element(date_locator)
        self.click_on_element(date_locator)

    @allure.step("Выбрать дату на календаре")
    def select_calendar_date(self, date):
        calendar_locator = OrderPageLocators.calendar_date(date)
        self.find_element(calendar_locator).click()

    @allure.step("Закрыть попап с куки")
    def close_cookies_popup(self):
        try:
            self.wait_for_element(OrderPageLocators.COCKIE_BUTTON)
            self.click_on_element(OrderPageLocators.COCKIE_BUTTON)
        except:
            pass

    @allure.step("Заполнить поля заказа")
    def fill_order_data(self, name, last_name, address, station_name, phone, delivery_date, period, color, comment):
        self.close_cookies_popup()
        self.enter_text(OrderPageLocators.NAME_INPUT, name)
        self.enter_text(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.enter_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.select_metro_station(station_name)
        self.enter_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click_next_button()
        self.enter_text(OrderPageLocators.WHEN_INPUT, delivery_date)
        self.select_rent_period(period)
        color_locator = OrderPageLocators.vehicle_color(color)
        self.click_on_element(color_locator)
        self.enter_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Нажать на кнопку Заказать")
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_FORM_BUTTON)

    @allure.step("Нажать на кнопку подтверждения заказа")
    def click_confirm_order_button(self):
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Сравнить текст окна подтверждения заказа")
    def compare_confirm_text(self, expected_text):
        self.wait_for_element(OrderPageLocators.CONFIRM_WINDOW)
        text = self.get_text(OrderPageLocators.CONFIRM_WINDOW)
        assert text == expected_text

    @allure.step("Проверить, что окно подтверждения заказа появилось")
    def is_confirm_window_visible(self, timeout=20):
        element = self.wait_for_element(OrderPageLocators.CONFIRM_WINDOW)
        assert element.is_displayed(), "Окно подтверждения заказа не появилось"
