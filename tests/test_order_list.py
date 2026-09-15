import allure
import pytest

from methods.order_methods import OrderMethods

@allure.feature('Список заказов')
class TestOrderList:

    @allure.title('В тело ответа возвращается список заказов')
    def test_get_orders_returns_list(self):
        response = OrderMethods.get_orders()

        assert response.status_code == 200
        body = response.json()
        assert 'orders' in body
        assert isinstance(body['orders'], list)