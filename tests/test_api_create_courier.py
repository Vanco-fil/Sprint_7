import allure
import requests
from data import Urls, Message
from helpers import register_new_courier_and_return_login_password


class TestCreateCourier:

    @allure.title('Проверка создания курьера со всеми обязательными полями')
    def test_create_courier(self, create_courier):
        resp = requests.post(Urls.CREATE_COURIER, data=create_courier)
        assert resp.status_code == 201 and resp.text == Message.RESPONSE_SUCCESS

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    def test_cannot_create_duplicate_courier(self):
        payload = register_new_courier_and_return_login_password()
        requests.post(Urls.CREATE_COURIER, data=payload)
        duplicate_courier = requests.post(Urls.CREATE_COURIER, data=payload)
        assert duplicate_courier.status_code == 409 and duplicate_courier.json()['message'] == Message.CONFLICT_LOGIN

    @allure.title('Проверка создания курьера без логина')
    def test_create_courier_without_login(self):
        payload = register_new_courier_and_return_login_password()
        payload['login'] = ''
        resp = requests.post(Urls.CREATE_COURIER, data=payload)
        assert resp.status_code == 400 and resp.json()['message'] == Message.INSUFFICIENT_INFO

    @allure.title('Проверка создания курьера без пароля')
    def test_create_courier_without_password(self):
        payload = register_new_courier_and_return_login_password()
        payload['password'] = ''
        resp = requests.post(Urls.CREATE_COURIER, data=payload)
        assert resp.status_code == 400 and resp.json()['message'] == Message.INSUFFICIENT_INFO
