import pytest
import allure
from pages.order_page import OrderActions

class TestOrderButtons:
    @allure.title('Проверка кнопок "Заказать" на главной странице')
    @allure.description('Проверка кнопки {button}')
    @pytest.mark.parametrize("button", ['top', 'bottom'])
    def test_order_button_click(self, driver, button):
        order_actions = OrderActions(driver)
        assert "Для кого самокат" in order_actions.check_form1_header(button)
