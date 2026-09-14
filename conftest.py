import pytest
import requests

from generators.generators import register_new_courier_and_return_login_password, generate_order_payload
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods

@pytest.fixture
def new_courier():
    '''Создание нового курьера и удаление его данных'''

    login_pass = register_new_courier_and_return_login_password()

    login, password, first_name = login_pass[0], login_pass[1], login_pass[2]

    login_response = CourierMethods.login_courier({
        'login': login,
        'password': password
    })
    courier_id = login_response.json()['id']

    yield {
        'login': login,
        'password': password,
        'firstName': first_name,
        'id': courier_id
    }

    CourierMethods.delete_courier(courier_id)

@pytest.fixture
def created_order():
    '''Создание заказа'''

    payload = generate_order_payload()
    response = OrderMethods.create_order(payload)
    track = response.json()['track']

    yield {'track': track, 'payload': payload}
