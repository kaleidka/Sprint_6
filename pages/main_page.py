import allure
from selenium.webdriver.common.keys import Keys
from locators.main_page_locators import MainPageSelectors, IconSelectors
from pages.base_page import BaseActions
from data import Urls

class MainPage(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Прокрутка до конца страницы")
    def scroll_down(self):
        scroll_element = self.find_element(MainPageSelectors.SCROLL_ELEMENT)
        scroll_element.send_keys(Keys.END)

    @allure.step("Прокрутка до элемента")
    def scroll_to_element(self, element):
        self.execute_js("arguments[0].scrollIntoView();", element)

    @allure.step("Клик по элементу через JS")
    def js_click(self, element):
        self.execute_js("arguments[0].click();", element)

    @allure.step("Получение текста ответа на вопрос")
    def get_faq_answer(self, question_number):
        self.open(Urls.main_page)
        self.scroll_down()

        question_locator = self.format_selector(MainPageSelectors.FAQ_BUTTON, question_number)
        answer_locator = self.format_selector(MainPageSelectors.ANSWER_TEXT, question_number)

        question_element = self.find_element(question_locator)
        self.scroll_to_element(question_element)
        self.js_click(question_element)

        return self.find_element(answer_locator).text

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.open(Urls.main_page)
        self.click_element(IconSelectors.SCOOTER_LOGO)
        return self.find_element(IconSelectors.MAIN_PAGE_TEXT).text

    @allure.step("Клик на ссылку Яндекс и переход на новую вкладку")
    def click_yandex_link(self):
        self.open(Urls.main_page)
        self.click_element(IconSelectors.YANDEX_LINK)
        self.switch_to_new_window()
        self.wait_for_url(Urls.yandex_dzen)

    @allure.step("Получение текущего URL")
    def current_url(self):
        return self.driver.current_url