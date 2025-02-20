import allure
from pages.main_page import MainPage
from data import Urls

class TestIconInteractions:
    @allure.title('Проверка кнопки Самокат')
    @allure.description('Проверка клика по кнопке Самокат')
    def test_scooter_logo_click(self, driver):
        main_page = MainPage(driver)
        assert 'когда накатаетесь — заберём' in main_page.click_scooter_logo()

    @allure.title('Проверка кнопки Яндекс')
    @allure.description('Проверка кнопки Яндекс')
    def test_yandex_link_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_link()
        assert Urls.yandex_dzen in main_page.current_url()
