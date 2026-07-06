import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LogoPage(BasePage):
    
    # Локаторы
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Заказать']")
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')


    @allure.step('Принятие cookies')
    def accept_cookie(self):
        self.scroll_to_element(self.COOKIE_BUTTON)
        self.click(self.COOKIE_BUTTON)


    @allure.step('Нажатие кнопки "Заказать"')
    def click_on_order_button(self):
        self.scroll_to_element(self.ORDER_BUTTON)
        self.click(self.ORDER_BUTTON)


    @allure.step("Клик по логотипу Самоката")
    def click_on_scooter_logo(self):
        self.scroll_to_element(self.SCOOTER_LOGO)
        self.click(self.SCOOTER_LOGO)


    @allure.step("Клик по логотипу Яндекса")
    def click_on_yandex_logo(self):
        self.scroll_to_element(self.YANDEX_LOGO)
        self.click(self.YANDEX_LOGO)
        