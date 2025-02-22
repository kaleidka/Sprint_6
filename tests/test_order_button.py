import pytest
import allure
from pages.order_page import OrderActions

@allure.feature("Проверка кнопок оформления заказа")
class TestOrderButtons:
    @pytest.mark.parametrize("button", ['top', 'bottom'])
    @allure.title('Проверка кнопки "Заказать" ({button})')
    @allure.description('Проверка клика по кнопке "Заказать" и перехода на форму заказа')
    def test_order_button_click(self, driver, button):
        order_actions = OrderActions(driver)
        form_header = order_actions.check_form1_header(button)
        assert "Для кого самокат" in form_header, (
            f"Ожидаемый заголовок формы не найден. Фактический заголовок: {form_header}"
        )