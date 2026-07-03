import random
import string


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_courier_data():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }


COURIER_WITHOUT_LOGIN = {
    "password": "3333",
    "firstName": "Sidor"
}


COURIER_WITHOUT_PASSWORD = {
    "login": "Sidor"
}


LOGIN_WITHOUT_LOGIN = {
    "password": "3333"
}


LOGIN_WITHOUT_PASSWORD = {
    "login": "Sidor"
}


ORDER_DATA = {
    "firstName": "Rajan",
    "lastName": "Gosling",
    "address": "Tambov",
    "metroStation": 3,
    "phone": "+7 800 555 35 35",
    "rentTime": 3,
    "deliveryDate": "2026-07-07",
    "comment": "Spasibo towarisch"
}
