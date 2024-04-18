import logging
import os
import requests
from faker import Faker

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def base_httpbin_url():
    return os.getenv("API_BASE_URL", "https://httpbin.org")


@pytest.fixture(scope="session")
def base_reqres_url():
    return os.getenv("API_BASE_URL", "https://reqres.in")


def pytest_configure(config):
    logging.basicConfig(level=logging.INFO)


pytest.mark.api = pytest.mark.mark(name="api")
pytest.mark.images = pytest.mark.mark(name="images")
pytest.mark.listUsers = pytest.mark.mark(name="listUsers")
pytest.mark.singleUser = pytest.mark.mark(name="singleUser")
pytest.mark.createUsers = pytest.mark.mark(name="createUsers")
pytest.mark.updateUsers = pytest.mark.mark(name="updateUsers")
pytest.mark.deleteUsers = pytest.mark.mark(name="deleteUsers")