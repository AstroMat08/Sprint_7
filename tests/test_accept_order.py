import allure
import pytest

from data.messages import ORDER_NOT_FOUND
from methods.order_methods import OrderMethods


@allure.feature('Принятие заказа')
class TestAcceptOrder:

    @allure.title('Успешное принятие заказа')
    def test_accept_order_success(self, created_order, new_courier):
        order_response = OrderMethods.get_order_by_track(created_order['track'])
        order_id = order_response.json()['order']['id']

        response = OrderMethods.accept_order(order_id, new_courier['id'])

        assert response.status_code == 200
        assert response.json() == {'ok': True}

    @allure.title('Ошибка при отсутствии id курьера')
    def test_accept_order_without_courier_id(self, created_order):
        order_response = OrderMethods.get_order_by_track(created_order['track'])
        order_id = order_response.json()['order']['id']

        response = OrderMethods.accept_order_without_courier_id(order_id)

        assert response.status_code == 400

    @allure.title('Ошибка при неверном id курьера')
    def test_accept_order_invalid_courier_id(self, created_order):
        order_response = OrderMethods.get_order_by_track(created_order['track'])
        order_id = order_response.json()['order']['id']

        response = OrderMethods.accept_order(order_id, 999999999)

        assert response.status_code == 404

    @allure.title('Ошибка при отсутствии id заказа')
    def test_accept_order_without_order_id(self, new_courier):
        response = OrderMethods.accept_order_without_order_id(new_courier['id'])

        assert response.status_code in (400, 404)

    @allure.title('Ошибка при неверном id заказа')
    def test_accept_order_invalid_order_id(self, new_courier):
        response = OrderMethods.accept_order(999999999, new_courier['id'])

        assert response.status_code == 404
        assert response.json()['message'] == ORDER_NOT_FOUND