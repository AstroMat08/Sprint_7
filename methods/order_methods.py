import requests

from data.urls import BASE_URL, CREATE_ORDER, GET_ORDER_LIST, ACCEPT_ORDER, GET_ORDER_BY_TRACK

class OrderMethods:

    @staticmethod
    def create_order(payload):
        return requests.post(f'{BASE_URL}{CREATE_ORDER}', json=payload)

    @staticmethod
    def get_orders():
        return requests.get(f'{BASE_URL}{GET_ORDER_LIST}')

    @staticmethod
    def accept_order(order_id, courier_id):
        # ID заказа — в пути, ID курьера — в query params
        params = {'courierId': courier_id}
        return requests.put(
            f'{BASE_URL}{ACCEPT_ORDER.format(order_id)}', params=params
        )

    @staticmethod
    def accept_order_without_courier_id(order_id):
        return requests.put(f'{BASE_URL}{ACCEPT_ORDER.format(order_id)}')

    @staticmethod
    def accept_order_without_order_id(courier_id):
        params = {'courierId': courier_id}
        return requests.put(f'{BASE_URL}/api/v1/orders/accept/', params=params)

    @staticmethod
    def get_order_by_track(track):
        return requests.get(
            f'{BASE_URL}{GET_ORDER_BY_TRACK}', params={'t': track}
        )

    @staticmethod
    def get_order_by_track_without_track():
        return requests.get(f'{BASE_URL}{GET_ORDER_BY_TRACK}')