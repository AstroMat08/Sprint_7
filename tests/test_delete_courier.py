import allure
import pytest

from methods.courier_methods import CourierMethods
from data.messages import COURIER_DELETE_NOT_FOUND
from generators.generators import register_new_courier_and_return_login_password

@allure.feature('Удаление курьера')
class TestDeleteCourier:

    @allure.title('Успешное удаление курьера')
    def test_delete_courier_success(self):
        login_pass = register_new_courier_and_return_login_password()
        login, password = login_pass[0], login_pass[1]

        login_response = CourierMethods.login_courier({
            'login': login, 'password': password
        })
        courier_id = login_response.json()['id']

        response = CourierMethods.delete_courier(courier_id)

        assert response.status_code == 200
        assert response.json() == {'ok': True}

    @allure.title('Удаление курьера без id возвращает ошибку')
    def test_delete_courier_without_id(self):
        response = CourierMethods.delete_courier_without_id()

        assert response.status_code in (400, 404)

    @allure.title('Удаление курьера c несуществующим id возвращает ошибку')
    def test_delete_courier_with_invalid_id(self):
        response = CourierMethods.delete_courier(999999999)

        assert response.status_code == 404
        assert response.json()['message'] == COURIER_DELETE_NOT_FOUND