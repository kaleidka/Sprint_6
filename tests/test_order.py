import pytest
import allure
from pages.order_page import OrderActions
from data import OrderData

@allure.feature("Проверка процесса оформления заказа")
class TestOrderProcess:
    @pytest.mark.parametrize(OrderData.input_params, OrderData.data_set)
    @allure.title("Полная проверка процесса заказа")
    @allure.description("Проверка оформления заказа с данными: {name}, {surname}, {address}, {metro}, {phone}, {date}, {period}, {color}, {comment}")
    def test_complete_order(self, driver, button, name, surname, address, metro, phone, date, period, color, comment):
        order_actions = OrderActions(driver)
        order_actions.complete_order(button, name, surname, address, metro, phone, date, period, color, comment)
        success_message = order_actions.check_success_message()
        assert "Заказ оформлен" in success_message, (
            f"Ожидаемое сообщение об успешном заказе не найдено. Фактическое сообщение: {success_message}"
        )