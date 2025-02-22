import allure
from pages.main_page import MainPage
from data import Urls

@allure.feature("Проверка взаимодействия с иконками")
class TestIconInteractions:
    @allure.title('Проверка кнопки "Самокат"')
    @allure.description('Проверка клика по логотипу "Самокат" и возврата на главную страницу')
    def test_scooter_logo_click(self, driver):
        main_page = MainPage(driver)
        result_text = main_page.click_scooter_logo()
        assert 'когда накатаетесь — заберём' in result_text, (
            f"Ожидаемый текст не найден. Фактический текст: {result_text}"
        )

    @allure.title('Проверка кнопки "Яндекс"')
    @allure.description('Проверка перехода по ссылке "Яндекс" и открытия новой вкладки')
    def test_yandex_link_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_link()
        current_url = main_page.current_url()
        assert Urls.yandex_dzen in current_url, (
            f"Ожидаемый URL не найден. Фактический URL: {current_url}"
        )