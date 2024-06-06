import allure
import requests
from data import Urls, Message


class TestCreateCourier:

    @allure.title('Проверка создания курьера со всеми обязательными полями')
    def test_create_courier(self, generated_courier_data):
        resp = requests.post(Urls.CREATE_COURIER, data=generated_courier_data)
        assert resp.status_code == 201 and resp.text == Message.RESPONSE_SUCCESS

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    def test_cannot_create_duplicate_courier(self, generated_courier_data):
        requests.post(Urls.CREATE_COURIER, data=generated_courier_data)
        duplicate_courier = requests.post(Urls.CREATE_COURIER, data=generated_courier_data)
        assert duplicate_courier.status_code == 409 and duplicate_courier.json()['message'] == Message.CONFLICT_LOGIN

    @allure.title('Проверка создания курьера без логина')
    def test_create_courier_without_login(self, generated_courier_data):
        generated_courier_data['login'] = ''
        resp = requests.post(Urls.CREATE_COURIER, data=generated_courier_data)
        assert resp.status_code == 400 and resp.json()['message'] == Message.INSUFFICIENT_INFO

    @allure.title('Проверка создания курьера без пароля')
    def test_create_courier_without_password(self, generated_courier_data):
        generated_courier_data['password'] = ''
        resp = requests.post(Urls.CREATE_COURIER, data=generated_courier_data)
        assert resp.status_code == 400 and resp.json()['message'] == Message.INSUFFICIENT_INFO
