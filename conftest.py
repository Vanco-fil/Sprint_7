from random import random
import random
import string
import pytest
import requests
from data import Urls


@pytest.fixture(scope="function")
def create_courier(generated_courier_data):
    requests.post(Urls.CREATE_COURIER, data=generated_courier_data)

    def cleanup():
        response_post = requests.post(Urls.LOGIN, data=generated_courier_data)
        courier_id = response_post.json()['id']
        requests.delete(f'{Urls.DELETE_COURIER}/{courier_id}')

    yield generated_courier_data
    cleanup()


@pytest.fixture(scope="function")
def generated_courier_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload
