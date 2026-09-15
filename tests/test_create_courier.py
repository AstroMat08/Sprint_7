import allure
import pytest

from data.messages import COURIER_ALREADY_EXISTS, COURIER_NOT_ENOUGH_DATA
from generators.generators import generate_courier_payload, generate_random_string
from methods.courier_methods import CourierMethods

@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.title('Курьера можно создать')
    def test_create_courier_success(self, deleted_courier):
        
        response = deleted_courier['response']

        assert response.status_code == 201
        assert response.json() == {'ok': True}


    @allure.title('Нельзя создать одинаковых курьеров')
    def test_create_duplicate_courier(self, new_courier):
        payload = {
            'login': new_courier['login'],
            'password': new_courier['password'],
            'firstName': new_courier['firstName']
        }

        response = CourierMethods.create_courier(payload)

        assert response.status_code == 409
        assert response.json()['message'] == COURIER_ALREADY_EXISTS

    @allure.title('Нельзя создать курьера без обязательного поля: {missing_field}')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_missing_field(self, missing_field):
        payload = generate_courier_payload()
        payload.pop(missing_field)

        response = CourierMethods.create_courier(payload)

        assert response.status_code == 400
        assert response.json()['message'] == COURIER_NOT_ENOUGH_DATA

    @allure.title('Нельзя создать курьера с логином, который уже существует')
    def test_create_courier_existing_login(self, new_courier):
        payload = {
            'login': new_courier['login'],
            'password': generate_random_string(10)
        }

        response = CourierMethods.create_courier(payload)

        assert response.status_code == 409
        assert response.json()['message'] == COURIER_ALREADY_EXISTS