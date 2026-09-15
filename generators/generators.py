import requests
import random
import string


def register_new_courier_and_return_login_password():
    """Метод регистрации нового курьера возвращает список из логина и пароля.
    Если регистрация не удалась, возвращает пустой список.
    """

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        'login': login,
        'password': password,
        'firstName': first_name
    }

    response = requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/courier',
        data=payload
    )

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_courier_payload():
    """Генерирует payload курьера без отправки запроса."""
    return {
        'login': generate_random_string(10),
        'password': generate_random_string(10),
        'firstName': generate_random_string(10)
    }


def generate_order_payload(color=None):
    """Генерирует payload заказа. Если color=None — поле color не добавляется."""
    payload = {
        'firstName': 'Naruto',
        'lastName': 'Uchiha',
        'address': 'Konoha, 142 apt.',
        'metroStation': 4,
        'phone': '+7 800 355 35 35',
        'rentTime': 5,
        'deliveryDate': '2020-06-06',
        'comment': 'Saske, come back to Konoha',
    }
    if color is not None:
        payload['color'] = color
    return payload