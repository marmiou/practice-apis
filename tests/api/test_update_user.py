import logging

import pytest
import requests
from faker import Faker

LIST_API = "/api/users"
SINGLE_USER_API = "/api/user/"


class TestUpdateUser:

    @pytest.fixture(scope="session")
    def create_user_fixture(self, base_reqres_url):
        def _create_user():
            fake = Faker()
            url = base_reqres_url + LIST_API
            request_body = {"name": fake.name(), "job": fake.job()}
            response = requests.post(url, json=request_body)
            assert response.status_code == 201
            return response.json()

        return _create_user

    @pytest.mark.api
    @pytest.mark.updateUsers
    def test_put_created_user_success(self, base_reqres_url, create_user_fixture):
        response_data = create_user_fixture()
        logging.info(f"Get initial data: {response_data}")
        url = base_reqres_url + SINGLE_USER_API + response_data["id"]
        data = {
            "name": "Markella",
            "job": response_data["job"],
            "id": response_data["id"],
            "createdAt": response_data["createdAt"],
        }
        update_response = requests.put(url, data=data)
        update_response_data = update_response.json()
        logging.info(f"Update data response: {update_response_data}")
        assert update_response.status_code == 200
        assert update_response_data["name"] == "Markella"
        assert update_response_data["job"] == response_data["job"]

    @pytest.mark.api
    @pytest.mark.updateUsers
    def test_patch_created_user_success(self, base_reqres_url, create_user_fixture):
        response_data = create_user_fixture()
        url = base_reqres_url + SINGLE_USER_API + response_data["id"]
        data = {"name": "Georgia"}
        update_response = requests.patch(url, data=data)
        update_response_data = update_response.json()
        logging.info(f"Update data response: {update_response_data}")
        assert update_response.status_code == 200
        assert update_response_data["name"] == "Georgia"
