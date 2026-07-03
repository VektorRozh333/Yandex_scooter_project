import requests
import api.urls


class OrderAPI:

    @staticmethod
    def create_order(payload):
        return requests.post(
            api.urls.CREATE_ORDER,
            json=payload
        )


    @staticmethod
    def get_orders():
        return requests.get(
            api.urls.GET_ORDERS
        )
    