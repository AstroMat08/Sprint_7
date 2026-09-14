import allure
import pytest

from data.messages import COURIER_LOGIN_NOT_ENOUGH_DATA, COURIER_LOGIN_NOT_FOUND
from generators.generators import generate_random_string
from methods.courier_methods import CourierMethods

@allure.feature('Логин курьера')
class TestLoginCourier:

    @allure.feature('Курьер может авторизоваться')
    def test_login_courier_success(self, new_courier):
        response = CourierMethods.login_courier({
            'login': new_courier['login'],
            'password': new_courier['password']
        })

        assert response.status_code == 200
        assert 'id' in response.json()

    @pytest.mark.parametrize('missing_field, expected_codes', [
        ('login', (400,)),
        ('password', (400, 504)),
    ])
    def test_login_courier_missing_field(self, new_courier, missing_field, expected_codes):
        payload = {
            'login': new_courier['login'],
            'password': new_courier['password']
        }
        payload.pop(missing_field)

        response = CourierMethods.login_courier(payload)

        assert response.status_code in expected_codes

        if response.status_code == 400: 
            assert response.json()['message'] == COURIER_LOGIN_NOT_ENOUGH_DATA
        else:
            assert 'Service unavailable' in response.text

    @allure.title('Ошибка при неверном логине')
    def test_login_wrong_login(self, new_courier):
        response = CourierMethods.login_courier({
            'login': generate_random_string(10),
            'password': new_courier['password']
        })

        assert response.status_code == 404
        assert response.json()['message'] == COURIER_LOGIN_NOT_FOUND

    @allure.title('Ошибка при неверном пароле')
    def test_login_wrong_login(self, new_courier):
        response = CourierMethods.login_courier({
            'login': new_courier['login'],
            'password': generate_random_string(10)
        })

        assert response.status_code == 404
        assert response.json()['message'] == COURIER_LOGIN_NOT_FOUND

    @allure.title('Ошибка при авторизации несуществующего пользователя')
    def test_login_nonexistent_user(self):
        response = CourierMethods.login_courier({
            'login': generate_random_string(10),
            'password': generate_random_string(10)
        })

        assert response.status_code == 404
        assert response.json()['message'] == COURIER_LOGIN_NOT_FOUND