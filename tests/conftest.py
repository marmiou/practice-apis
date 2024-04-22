import logging
import os

import pytest
import requests
from dotenv import load_dotenv
from faker import Faker

load_dotenv()


@pytest.fixture(scope="session")
def base_httpbin_url():
    return os.getenv("API_BASE_URL", "https://httpbin.org")


@pytest.fixture(scope="session")
def base_reqres_url():
    return os.getenv("API_BASE_URL", "https://reqres.in")


@pytest.fixture()
def create_user(base_reqres_url):
    fake = Faker()
    url = base_reqres_url + "/api/users"
    request_body = {"name": fake.name(), "job": fake.job()}
    response = requests.post(url, json=request_body)
    assert response.status_code == 201
    return response.json()


def pytest_configure(config):
    logging.basicConfig(level=logging.INFO)


pytest.mark.api = pytest.mark.mark(name="api")
pytest.mark.images = pytest.mark.mark(name="images")
pytest.mark.listUsers = pytest.mark.mark(name="listUsers")
pytest.mark.singleUser = pytest.mark.mark(name="singleUser")
pytest.mark.createUsers = pytest.mark.mark(name="createUsers")
pytest.mark.updateUsers = pytest.mark.mark(name="updateUsers")
pytest.mark.deleteUsers = pytest.mark.mark(name="deleteUsers")
