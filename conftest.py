import pytest
import requests
from data import Urls
from helpers import register_new_courier_and_return_login_password


@pytest.fixture(scope="function")
def create_courier():
    payload = register_new_courier_and_return_login_password()
    yield payload
    response_post = requests.post(Urls.LOGIN, data={"login": payload['login'], "password": payload['password']})
    courier_id = response_post.json()['id']
    requests.delete(f'{Urls.DELETE_COURIER}/{courier_id}')
