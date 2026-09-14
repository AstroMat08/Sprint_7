import pytest
import allure

from data.messages import ORDER_NOT_ENOUGH_DATA, ORDER_TRACK_NOT_FOUND
from methods.order_methods import OrderMethods


@allure.feature('Получение заказа по номеру')
class TestGetOrderByTrack:

    @allure.title('Успешное получение заказа по треку')
    def test_get_order_by_track_success(self, created_order):
        response = OrderMethods.get_order_by_track(created_order['track'])

        assert response.status_code == 200
        body = response.json()
        assert 'order' in body
        assert isinstance(body['order'], dict)

    @allure.title('Ошибка при запросе без номера заказа')
    def test_get_order_without_track(self):
        response = OrderMethods.get_order_by_track_without_track()

        assert response.status_code == 400
        assert response.json()['message'] == ORDER_NOT_ENOUGH_DATA

    @allure.title('Ошибка при несуществующем заказе')
    def test_get_order_nonexistent_track(self):
        response = OrderMethods.get_order_by_track(999999999)

        assert response.status_code == 404
        assert response.json()['message'] == ORDER_TRACK_NOT_FOUND