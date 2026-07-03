import requests
import api.urls


class CourierAPI:

    @staticmethod
    def create_courier(payload):
        return requests.post(
            api.urls.CREATE_COURIER,
            json=payload
        )


    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(
            api.urls.CREATE_COURIER
        )
    