import logging

import pytest
import requests
from faker import Faker

LIST_API = "/api/users"
SINGLE_USER_API = "/api/user/"


class TestUpdateUser:

    @pytest.mark.api
    @pytest.mark.updateUsers
    def test_put_created_user_success(self, base_reqres_url, create_user):
        response_data = create_user
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
    def test_patch_created_user_success(self, base_reqres_url, create_user):
        response_data = create_user
        url = base_reqres_url + SINGLE_USER_API + response_data["id"]
        data = {"name": "Georgia"}
        update_response = requests.patch(url, data=data)
        update_response_data = update_response.json()
        logging.info(f"Update data response: {update_response_data}")
        assert update_response.status_code == 200
        assert update_response_data["name"] == "Georgia"
