import allure
from api.courier_api import CourierAPI
import data


class TestCreateCourier:

    @allure.title('Создание курьера')
    def test_create_courier_success(self):

        courier = data.generate_courier_data()

        response = CourierAPI.create_courier(courier)

        assert response.status_code == 201
        assert response.json()["ok"] is True


    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self):

        courier = data.generate_courier_data()
        CourierAPI.create_courier(courier)

        response = CourierAPI.create_courier(courier)

        assert response.status_code == 409


    @allure.title('Создание курьера без логина')
    def test_create_courier_without_login(self):

        response = CourierAPI.create_courier(data.COURIER_WITHOUT_LOGIN)

        assert response.status_code == 400


    @allure.title('Создание курьера без пароля')
    def test_create_courier_without_password(self):

        response = CourierAPI.create_courier(data.COURIER_WITHOUT_PASSWORD)

        assert response.status_code == 400
