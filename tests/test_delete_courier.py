import allure
import pytest

from methods.courier_methods import CourierMethods
from data.messages import COURIER_DELETE_NOT_FOUND

@allure.feature('Удаление курьера')
class TestDeleteCourier:

    @allure.title('Успешное удаление курьера')
    def test_delete_courier_success(self, courier_for_delete):
        response = CourierMethods.delete_courier(courier_for_delete['id'])

        assert response.status_code == 200
        assert response.json() == {'ok': True}

    @allure.title('Удаление курьера без id возвращает ошибку')
    def test_delete_courier_without_id(self):
        response = CourierMethods.delete_courier_without_id()

        assert response.status_code == 404

    @allure.title('Удаление курьера c несуществующим id возвращает ошибку')
    def test_delete_courier_with_invalid_id(self):
        response = CourierMethods.delete_courier(999999999)

        assert response.status_code == 404
        assert response.json()['message'] == COURIER_DELETE_NOT_FOUND