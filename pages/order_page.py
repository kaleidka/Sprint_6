import allure
from locators.order_page_locators import OrderButtonSelectors, OrderStepOneSelectors, OrderStepTwoSelectors
from pages.base_page import BaseActions
from data import Urls

class OrderActions(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке заказа: {order_button}')
    def click_order_button(self, order_button):
        if order_button == 'top':
            self.click_element(OrderButtonSelectors.TOP_ORDER_BUTTON)
        elif order_button == 'bottom':
            bottom_button = self.find_element(OrderButtonSelectors.BOTTOM_ORDER_BUTTON)
            self.execute_js("arguments[0].scrollIntoView();", bottom_button)
            self.click_element(OrderButtonSelectors.BOTTOM_ORDER_BUTTON)

    @allure.step('Проверка заголовка первой формы заказа')
    def check_form1_header(self, order_button):
        self.open(Urls.main_page)
        self.click_order_button(order_button)
        return self.find_element(OrderStepOneSelectors.FORM_HEADER).text

    @allure.step('Заполнение поля "Станция метро"')
    def fill_metro_field(self, metro):
        self.click_element(OrderStepOneSelectors.METRO_FIELD)
        self.find_element(OrderStepOneSelectors.METRO_FIELD).send_keys(metro)
        self.click_element(OrderStepOneSelectors.METRO_DROPDOWN)

    @allure.step('Заполнение формы "Даты"')
    def fill_date_field(self, date):
        self.find_element(OrderStepTwoSelectors.DATE_FIELD).send_keys(date)
        formatted_date = self.format_selector(OrderStepTwoSelectors.DAY_SELECT, date)
        self.click_element(formatted_date)

    @allure.step('Заполнение формы "Срок аренды"')
    def fill_period_field(self, period):
        self.click_element(OrderStepTwoSelectors.PERIOD_FIELD)
        self.click_element(self.format_selector(OrderStepTwoSelectors.DATE_SELECT, period))

    @allure.step('Выбор цвета')
    def select_color(self, color):
        color_id = 'black' if color == 'чёрный жемчуг' else 'grey'
        self.click_element(self.format_selector(OrderStepTwoSelectors.COLOR_SELECT, color_id))

    @allure.step('Проверка заголовка окна успешного заказа')
    def check_success_message(self):
        return self.find_element(OrderStepTwoSelectors.SUCCESS_MESSAGE).text

    @allure.step('Заполнение и подтверждение заказа')
    def complete_order(self, button, name, surname, address, metro, phone, date, period, color, comment):
        self.open(Urls.main_page)
        self.click_order_button(button)
        self.find_element(OrderStepOneSelectors.FORM_HEADER)
        self.find_element(OrderStepOneSelectors.NAME_FIELD).send_keys(name)
        self.find_element(OrderStepOneSelectors.SURNAME_FIELD).send_keys(surname)
        self.find_element(OrderStepOneSelectors.ADDRESS_FIELD).send_keys(address)
        self.fill_metro_field(metro)
        self.find_element(OrderStepOneSelectors.PHONE_FIELD).send_keys(phone)
        self.click_element(OrderStepOneSelectors.NEXT_BUTTON)
        self.find_element(OrderStepTwoSelectors.FORM_HEADER)
        self.fill_date_field(date)
        self.fill_period_field(period)
        self.select_color(color)
        self.find_element(OrderStepTwoSelectors.COMMENT_FIELD).send_keys(comment)
        self.click_element(OrderStepTwoSelectors.ORDER_BUTTON)
        self.click_element(OrderStepTwoSelectors.CONFIRM_BUTTON)