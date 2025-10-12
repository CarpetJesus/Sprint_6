import allure
from Locators.order_page_locators import OrderPageLocators
from Pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Заполнить имя"):
    def fill_name(self):
        self.enter_text(OrderPageLocators.NAME_INPUT, name)

    @allure.step("Заполнить фамилию"):
    def fill_surname(self):
        self.enter_text(OrderPageLocators.LAST_NAME_INPUT, last_name)

    @allure.step("Заполнить адрес"):
    def fill_address(self):
        self.enter_text(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step("Выбрать станию метро"):
    def select_metro_station(self):
        self.click_on_element(OrderPageLocators.METRO_INPUT)
        station = self.scroll_to_element(OrderPageLocators.METRO_LIST)
        self.click_on_element(station)

    @allure.step("Заполнить номер телефона"):
    def fill_phone(self):
        self.enter_text(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Нажать на кнопку Далее"):
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.CONTINUE_BUTTON)

    @allure.step("Ввести дату"):
    def fill_date(self):
        self.enter_text(OrderPageLocators.WHEN_INPUT, date)

    @allure.step("Выбрать срок аренды"):
    def select_rent_period(self):
        self.click_on_element(OrderPageLocators.ORDER_DATE_FORM)
        self.scroll_to_element(OrderPageLocators.ORDER_DATE)
        self.click_on_element(OrderPageLocators.ORDER_DATE)

    @allure.step("Выбрать цвет самоката"):
    def select_color(self):
        self.click_on_element(OrderPageLocators.VEHICLE_COLOR)

    @allure.step("Заполнить комментарий"):
    def fill_comment(self):
        self.enter_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Нажать на кнопку Заказать"):
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_FORM_BUTTON)

    @allure.step("Нажать на кнопку подтверждения заказа"):
    def click_confirm_order_button(self):
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Сравнить текст окна подтверждения заказа"):
    def compare_confirm_text(self, expected_text):
        text = self.get_text(OrderPageLocators.CONFIRM_WINDOW)
        assert text == expected_text

