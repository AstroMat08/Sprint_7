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

    @allure.title('Нельзя авторизоваться без логина')
    def test_login_courier_without_login(self, new_courier):
        response = CourierMethods.login_courier({
            'password': new_courier['password']
        })

        assert response.status_code == 400
        assert response.json()['message'] == COURIER_LOGIN_NOT_ENOUGH_DATA


    @allure.title('Нельзя авторизоваться без пароля')
    @pytest.mark.skip(reason='Стенд возвращает 504 вместо 400 — известный баг')
    def test_login_courier_without_password(self, new_courier):
        response = CourierMethods.login_courier({
            'login': new_courier['login']
        })

        assert response.status_code == 400
        assert response.json()['message'] == COURIER_LOGIN_NOT_ENOUGH_DATA

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