import allure
import requests
from data import Urls, Message
from helpers import register_new_courier_and_return_login_password


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера со всеми обязательными полями')
    def test_create_courier(self, create_courier):
        requests.post(Urls.CREATE_COURIER, data=create_courier)
        resp = requests.post(Urls.LOGIN, data=create_courier)
        assert resp.status_code == 200 and 'id' in resp.text

    @allure.title('Проверка авторизации курьера без логина')
    def test_authorization_without_login(self):
        payload = register_new_courier_and_return_login_password()
        requests.post(Urls.CREATE_COURIER, data=payload)
        payload['login'] = ''
        resp = requests.post(Urls.LOGIN, data=payload)
        assert resp.status_code == 400 and resp.json()['message'] == Message.INSUFFICIENT_LOGIN

    @allure.title('Проверка авторизации курьера без пароля')
    def test_authorization_without_password(self):
        payload = register_new_courier_and_return_login_password()
        requests.post(Urls.CREATE_COURIER, data=payload)
        payload['password'] = ''
        resp = requests.post(Urls.LOGIN, data=payload)
        assert resp.status_code == 400 and resp.json()['message'] == Message.INSUFFICIENT_LOGIN

    @allure.title('Проверка авторизации под несуществующим курьером')
    def test_authorization_defunct_courier(self):
        payload = register_new_courier_and_return_login_password()
        resp = requests.post(Urls.LOGIN, data=payload)
        assert resp.status_code == 404 and resp.json()['message'] == Message.INVALID_DATA
