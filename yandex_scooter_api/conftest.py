import pytest
import data
from api.courier_api import CourierAPI


@pytest.fixture
def create_new_courier():

    courier = data.generate_courier_data()

    CourierAPI.create_courier(courier)

    login_data = {
        "login": courier["login"],
        "password": courier["password"]
    }

    login_response = CourierAPI.login_courier(login_data)

    courier_id = login_response.json()["id"]

    yield courier

    CourierAPI.delete_courier(courier_id)
