import allure
import pytest
import requests
from data import Urls, PersonalDate


class TestCreateOrder:
    person_data = PersonalDate.personal_date

    @pytest.mark.parametrize(
        "firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color", person_data)
    @allure.title('Проверка создания заказа с цветом и без него')
    def test_create_order_with_color(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate,
                                     comment, color):
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": [color],
        }
        resp = requests.post(Urls.CREATE_ORDERS, json=payload)
        assert resp.status_code == 201 and 'track' in resp.text
