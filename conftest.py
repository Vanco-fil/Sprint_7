import pytest
import requests
from data import Urls
from helpers import generated_data_new_courier_and_return_login_password


@pytest.fixture(scope="function")
def create_courier():
    payload = generated_data_new_courier_and_return_login_password()
    requests.post(Urls.CREATE_COURIER, data=payload)
    yield payload
    response_post = requests.post(Urls.LOGIN, data=payload)
    courier_id = response_post.json()['id']
    requests.delete(f'{Urls.DELETE_COURIER}/{courier_id}')
