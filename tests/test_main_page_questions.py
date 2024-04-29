import pytest
from data import *
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocator
from conftest import driver



class TestQuestionsMainPage:
    @allure.title('Проверяем вопросы и ответы на главной странице')
    @allure.description(
        'Кликаем на вопросы по порядку и проверяем ответы в выпадающем списке')
    @pytest.mark.parametrize('question_num, expected_reply', trueAnswer)
    def test_questions(self, driver, question_num, expected_reply):
        main_page = MainPage(driver)
        main_page.click_on_cookie_button()
        main_page.scrolling_to_questions()
        main_page.click_important_question(question_num)
        reply = main_page.get_important_reply(question_num)
        assert reply == expected_reply