import allure
import requests
from data import Urls, Message


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера со всеми обязательными полями')
    def test_create_courier(self, create_courier):
        resp = requests.post(Urls.LOGIN, data=create_courier)
        assert resp.status_code == 200 and 'id' in resp.text

    @allure.title('Проверка авторизации курьера без логина')
    def test_authorization_without_login(self, generated_courier_data):
        requests.post(Urls.CREATE_COURIER, data=generated_courier_data)
        generated_courier_data['login'] = ''
        resp = requests.post(Urls.LOGIN, data=generated_courier_data)
        assert resp.status_code == 400 and resp.json()['message'] == Message.INSUFFICIENT_LOGIN

    @allure.title('Проверка авторизации курьера без пароля')
    def test_authorization_without_password(self, generated_courier_data):
        requests.post(Urls.CREATE_COURIER, data=generated_courier_data)
        generated_courier_data['password'] = ''
        resp = requests.post(Urls.LOGIN, data=generated_courier_data)
        assert resp.status_code == 400 and resp.json()['message'] == Message.INSUFFICIENT_LOGIN

    @allure.title('Проверка авторизации под несуществующим курьером')
    def test_authorization_defunct_courier(self, generated_courier_data):
        resp = requests.post(Urls.LOGIN, data=generated_courier_data)
        assert resp.status_code == 404 and resp.json()['message'] == Message.INVALID_DATA
