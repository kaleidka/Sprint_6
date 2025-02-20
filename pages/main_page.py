import allure
import time
from selenium.webdriver.common.keys import Keys
from locators.main_page_locators import MainPageSelectors, IconSelectors
from pages.base_page import BaseActions
from data import Urls

class MainPage:
    def __init__(self, driver):
        self.actions = BaseActions(driver)

    @allure.step("Прокрутка до конца страницы")
    def scroll_down(self):
        self.actions.find_element(MainPageSelectors.SCROLL_ELEMENT).send_keys(Keys.END)

    @allure.step("Прокрутка до элемента")
    def scroll_to_element(self, element):
        self.actions.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Клик по элементу через JS")
    def js_click(self, element):
        self.actions.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получение текста ответа на вопрос")
    def get_faq_answer(self, question_number):
        self.actions.open(Urls.main_page)
        self.scroll_down()

        question_locator = self.actions.format_selector(MainPageSelectors.FAQ_BUTTON, question_number)
        answer_locator = self.actions.format_selector(MainPageSelectors.ANSWER_TEXT, question_number)

        element = self.actions.find_element(question_locator)
        self.scroll_to_element(element)
        self.js_click(element)

        return self.actions.find_element(answer_locator).text

    def click_scooter_logo(self):
        self.actions.open(Urls.main_page)
        self.actions.click_element(IconSelectors.SCOOTER_LOGO)
        return self.actions.find_element(IconSelectors.MAIN_PAGE_TEXT).text

    def click_yandex_link(self):
        self.actions.open(Urls.main_page)
        self.actions.click_element(IconSelectors.YANDEX_LINK)
        time.sleep(7)
        self.actions.switch_to_new_window()
        self.actions.wait_for_url(Urls.yandex_dzen)

    def current_url(self):
        return self.actions.driver.current_url
