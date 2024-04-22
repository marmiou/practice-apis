import logging

import pytest
import requests
from faker import Faker

LIST_API = "/api/users"
SINGLE_USER_API = "/api/user/"


class TestDeleteUser:
    @pytest.mark.api
    @pytest.mark.deleteUsers
    def test_delete_created_user_success(self, base_reqres_url, create_user):
        response_data = create_user
        user_url = base_reqres_url + SINGLE_USER_API + f"/{response_data['id']}"
        response = requests.delete(user_url)
        assert response.status_code == 204
