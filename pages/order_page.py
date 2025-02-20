import allure
from locators.order_page_locators import OrderButtonSelectors, OrderStepOneSelectors, OrderStepTwoSelectors
from pages.base_page import BaseActions
from data import Urls

class OrderActions:
    def __init__(self, driver):
        self.actions = BaseActions(driver)

    @allure.step('Клик по кнопке заказа: {order_button}')
    def click_order_button(self, order_button):
        if order_button == 'top':
            self.actions.click_element(OrderButtonSelectors.TOP_ORDER_BUTTON)
        elif order_button == 'bottom':
            bottom_button = self.actions.find_element(OrderButtonSelectors.BOTTOM_ORDER_BUTTON)
            self.actions.execute_js("arguments[0].scrollIntoView();", bottom_button)
            self.actions.click_element(OrderButtonSelectors.BOTTOM_ORDER_BUTTON)

    @allure.step('Проверка заголовка первой формы заказа')
    def check_form1_header(self, order_button):
        self.actions.open(Urls.main_page)
        self.click_order_button(order_button)
        return self.actions.find_element(OrderStepOneSelectors.FORM_HEADER).text

    @allure.step('Заполнение поля "Станция метро"')
    def fill_metro_field(self, metro):
        self.actions.click_element(OrderStepOneSelectors.METRO_FIELD)
        self.actions.find_element(OrderStepOneSelectors.METRO_FIELD).send_keys(metro)
        self.actions.click_element(OrderStepOneSelectors.METRO_DROPDOWN)

    @allure.step('Заполнение формы "Даты"')
    def fill_date_field(self, date):
        self.actions.find_element(OrderStepTwoSelectors.DATE_FIELD).send_keys(date)
        formatted_date = self.actions.format_selector(OrderStepTwoSelectors.DAY_SELECT, date)
        self.actions.click_element(formatted_date)

    @allure.step('Заполнение формы "Срок аренды"')
    def fill_period_field(self, period):
        self.actions.click_element(OrderStepTwoSelectors.PERIOD_FIELD)
        self.actions.click_element(self.actions.format_selector(OrderStepTwoSelectors.DATE_SELECT, period))

    @allure.step('Выбор цвета')
    def select_color(self, color):
        color_id = 'black' if color == 'чёрный жемчуг' else 'grey'
        self.actions.click_element(self.actions.format_selector(OrderStepTwoSelectors.COLOR_SELECT, color_id))

    @allure.step('Проверка заголовка окна успешного заказа')
    def check_success_message(self):
        return self.actions.find_element(OrderStepTwoSelectors.SUCCESS_MESSAGE).text

    def complete_order(self, button, name, surname, address, metro, phone, date, period, color, comment):
        self.actions.open(Urls.main_page)
        self.click_order_button(button)
        self.actions.find_element(OrderStepOneSelectors.FORM_HEADER)
        self.actions.find_element(OrderStepOneSelectors.NAME_FIELD).send_keys(name)
        self.actions.find_element(OrderStepOneSelectors.SURNAME_FIELD).send_keys(surname)
        self.actions.find_element(OrderStepOneSelectors.ADDRESS_FIELD).send_keys(address)
        self.fill_metro_field(metro)
        self.actions.find_element(OrderStepOneSelectors.PHONE_FIELD).send_keys(phone)
        self.actions.click_element(OrderStepOneSelectors.NEXT_BUTTON)
        self.actions.find_element(OrderStepTwoSelectors.FORM_HEADER)
        self.fill_date_field(date)
        self.fill_period_field(period)
        self.select_color(color)
        self.actions.find_element(OrderStepTwoSelectors.COMMENT_FIELD).send_keys(comment)
        self.actions.click_element(OrderStepTwoSelectors.ORDER_BUTTON)
        self.actions.click_element(OrderStepTwoSelectors.CONFIRM_BUTTON)
