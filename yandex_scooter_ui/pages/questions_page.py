import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class QuestionsPage(BasePage):
    
    QUESTIONS = [
        (By.XPATH, ".//div[@id='accordion__heading-0']"),
        (By.XPATH, ".//div[@id='accordion__heading-1']"),
        (By.XPATH, ".//div[@id='accordion__heading-2']"),
        (By.XPATH, ".//div[@id='accordion__heading-3']"),
        (By.XPATH, ".//div[@id='accordion__heading-4']"),
        (By.XPATH, ".//div[@id='accordion__heading-5']"),
        (By.XPATH, ".//div[@id='accordion__heading-6']"),
        (By.XPATH, ".//div[@id='accordion__heading-7']"),
    ]
    
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')

    @allure.step('Принятие cookies')
    def accept_cookie(self):
        self.scroll_to_element(self.COOKIE_BUTTON)
        self.click(self.COOKIE_BUTTON)

    @allure.step("Клик по вопросу №{index}")
    def click_question_by_index(self, index):
        """
        Универсальный метод для клика по вопросу.
        index: порядковый номер вопроса (начиная с 0)
        """
        locator = self.QUESTIONS[index]
        self.scroll_to_element(locator)
        self.wait_element(locator)
        