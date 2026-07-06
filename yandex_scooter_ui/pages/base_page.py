import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from abc import ABC


class BasePage(ABC):
    
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Открытие страницы {url}')
    def open(self, url):
        self.driver.get(url)


    @allure.step('Проверка названия сайта')
    def get_title(self):
        return self.driver.title


    @allure.step('Ожидание элемента')
    def wait_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )


    @allure.step('Ожидание кликабельности элемента')
    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )


    @allure.step('Клик по элементу')
    def click(self, locator):
        self.wait_clickable(locator).click()

    @allure.step('Ввод текста')
    def send_keys(self, locator, text):
        self.wait_element(locator).send_keys(text)


    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )
