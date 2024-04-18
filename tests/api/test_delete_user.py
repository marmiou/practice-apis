import logging
import pytest
import requests
from faker import Faker

LIST_API = '/api/users'
SINGLE_USER_API = '/api/user/'


class TestDeleteUser:
    @pytest.fixture(scope="session")
    def create_user_fixture(self,base_reqres_url):
        def _create_user():
            fake = Faker()
            url = base_reqres_url + LIST_API
            request_body = {"name": fake.name(), "job": fake.job()}
            response = requests.post(url, json=request_body)
            assert response.status_code == 201
            return response.json()
        return _create_user

    @pytest.mark.api
    @pytest.mark.deleteUsers
    def test_delete_created_user_success(self, base_reqres_url, create_user_fixture):
        response_data = create_user_fixture()
        user_url = base_reqres_url + SINGLE_USER_API + f"/{response_data['id']}"
        response = requests.delete(user_url)
        assert response.status_code == 204