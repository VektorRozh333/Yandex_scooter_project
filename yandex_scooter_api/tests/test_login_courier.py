import allure
from api.courier_api import CourierAPI
import data


class TestLoginCourier:

    @allure.title('Успешный логин курьера')
    def test_login_courier_success(self, create_new_courier):

        payload = {
            "login": create_new_courier["login"],
            "password": create_new_courier["password"]
        }

        response = CourierAPI.login_courier(payload)

        assert response.status_code == 200
        assert "id" in response.json()


    @allure.title('Логин без логина')
    def test_login_without_login(self):

        response = CourierAPI.login_courier(data.LOGIN_WITHOUT_LOGIN)

        assert response.status_code == 400


    @allure.title('Логин без пароля')
    def test_login_without_password(self):

        response = CourierAPI.login_courier(data.LOGIN_WITHOUT_PASSWORD)

        assert response.status_code in [400, 504]


    @allure.title('Логин несуществующего курьера')
    def test_login_nonexistent_courier(self):

        payload = {
            "login": "fake_user",
            "password": "fake_password"
        }

        response = CourierAPI.login_courier(payload)

        assert response.status_code == 404
