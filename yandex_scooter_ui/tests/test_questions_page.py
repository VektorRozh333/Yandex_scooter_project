import pytest
import allure
import data
from pages.questions_page import QuestionsPage


class TestQuestionsPage:
    
    with allure.step('Создаем список индексов для проверки'):
        QUESTIONS_TO_TEST = [0, 1, 2, 3, 4, 5, 6, 7]

    @allure.title("Проверка вопроса №{question_index}")
    @pytest.mark.parametrize("question_index", QUESTIONS_TO_TEST)
    def test_individual_question(self, driver, question_index):
        questions_page = QuestionsPage(driver)

        with allure.step('Открытие главной страницы'):
            questions_page.open(data.BASE_URL)
        
        with allure.step('Принятие cookie'):
            questions_page.accept_cookie()

        with allure.step(f'Клик по вопросу под индексом {question_index}'):
            questions_page.click_question_by_index(question_index)
