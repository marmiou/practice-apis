import logging

import pytest
import requests

LIST_API = "/api/users"
SINGLE_USER_API = "/api/user/"


class TestCreateUsers:

    @pytest.mark.api
    @pytest.mark.createUsers
    def test_create_users_json_should_return_created(self, base_reqres_url):
        url = base_reqres_url + LIST_API
        request_body = {"name": "Markella", "job": "QA Automation Engineer"}
        response = requests.post(url, json=request_body)
        assert response.status_code == 201

    def test_create_users_data_should_return_created(self, base_reqres_url):
        url = base_reqres_url + LIST_API
        request_data = {"name": "Markella", "job": "QA Automation Engineer"}
        response = requests.post(url, data=request_data)
        assert response.status_code == 201

    def test_get_created_user_should_return_success(self, base_reqres_url):
        url = base_reqres_url + LIST_API
        request_body = {"name": "Markella", "job": "QA Automation Engineer"}
        response = requests.post(url, json=request_body)
        response_data = response.json()
        assert response.status_code == 201
        single_user_url = base_reqres_url + SINGLE_USER_API
        get_user_response = requests.get(single_user_url, params=response_data["id"])
        assert get_user_response.status_code == 200
