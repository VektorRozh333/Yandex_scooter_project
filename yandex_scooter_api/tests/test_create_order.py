import pytest
import allure
from api.order_api import OrderAPI
import data


class TestCreateOrder:

    @pytest.mark.parametrize(
        'colors',
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []
        ]
    )

    
    @allure.title('Создание заказа с разными цветами')
    def test_create_order_with_different_colors(self, colors):

        order_body = data.ORDER_DATA.copy()

        order_body["color"] = colors

        response = OrderAPI.create_order(order_body)

        assert response.status_code == 201
        assert "track" in response.json()
