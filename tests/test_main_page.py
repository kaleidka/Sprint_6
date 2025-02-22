import pytest
import allure
from pages.main_page import MainPage
from data import QuestionsData

@allure.feature("Проверка вопросов и ответов на главной странице")
class TestMainPage:
    @pytest.mark.parametrize(QuestionsData.param, QuestionsData.value)
    @allure.title("Проверка ответа на вопрос № {question_number}")
    @allure.description("Клик по вопросу и проверка текста ответа")
    def test_faq_interaction(self, driver, question_number, expected_answer_text):
        main_page = MainPage(driver)
        actual_answer = main_page.get_faq_answer(question_number)
        assert expected_answer_text == actual_answer, (
            f"Ожидаемый ответ: {expected_answer_text}. Фактический ответ: {actual_answer}"
        )