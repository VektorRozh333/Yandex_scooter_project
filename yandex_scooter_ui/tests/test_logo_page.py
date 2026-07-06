import allure
import data
from pages.logo_page import LogoPage
from selenium.webdriver.support.ui import WebDriverWait


class TestLogoPage:
    
    @allure.title("Проверка перехода через кнопку заказа и логотип Самоката")
    def test_logo_is_avaliable(self, driver):
        logo_page = LogoPage(driver)

        logo_page.open(data.BASE_URL)

        with allure.step('Принятие cookie'):
            logo_page.accept_cookie()
        
        with allure.step('переход на заказ и обратно'):
            logo_page.click_on_order_button()
            logo_page.click_on_scooter_logo()

        with allure.step(f"Проверка, что текущий URL равен {data.BASE_URL}"):
            assert driver.current_url == data.BASE_URL, f"Expected {data.BASE_URL}, but got {driver.current_url}"


    @allure.title('Проверка логотипа Яндекса')
    def test_yandex_logo(self, driver):

        with allure.step('Открытие главной страницы'):
            driver.get(data.BASE_URL)

        logo_page = LogoPage(driver)

        with allure.step('Принятие cookie'):
            logo_page.accept_cookie()

        with allure.step('Нажатие на логотип Яндекса'):
            logo_page.click_on_yandex_logo()

        with allure.step('Ожидание открытия новой вкладки'):
            WebDriverWait(driver, 10).until(
                lambda d: len(d.window_handles) > 1
            )

        with allure.step('Переключение на новую вкладку'):
            driver.switch_to.window(driver.window_handles[1])

        with allure.step('Ожидание загрузки страницы'):
            WebDriverWait(driver, 15).until(
                lambda d: d.current_url != 'about:blank'
            )

        with allure.step('Проверка перехода'):
            print(driver.current_url)
            assert 'ya.ru' in driver.current_url.lower() or \
                'dzen' in driver.current_url.lower()
        