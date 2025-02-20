import pytest
import allure
from pages.order_page import OrderActions
from data import OrderData

class TestOrderProcess:
    @allure.title('Полная проверка процесса заказа')
    @allure.description('Полная проверка процесса заказа')
    @pytest.mark.parametrize(OrderData.input_params, OrderData.data_set)
    def test_complete_order(self, driver, button, name, surname, address, metro, phone, date, period, color, comment):
        order_actions = OrderActions(driver)
        order_actions.complete_order(button, name, surname, address, metro, phone, date, period, color, comment)
        assert "Заказ оформлен" in order_actions.check_success_message()
