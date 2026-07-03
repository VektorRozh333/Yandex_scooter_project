import allure
from api.order_api import OrderAPI


class TestGetOrders:

    @allure.title('Получение списка заказов')
    def test_get_orders(self):

        response = OrderAPI.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
