import allure
import pytest

from generators.generators import generate_order_payload
from methods.order_methods import OrderMethods

@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.feature('Создание заказа с цветом: {color}')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order_with_colors(self, color):
        payload = generate_order_payload(color)
        response = OrderMethods.create_order(payload)

        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Создание заказа без поля color')
    def test_create_order_without_color_field(self):
        payload = generate_order_payload()
        payload.pop('color', None)
        response = OrderMethods.create_order(payload)

        assert response.status_code == 201
        assert 'track' in response.json()