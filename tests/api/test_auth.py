import logging
import pytest
import requests

USERNAME = 'mark'
PASSWORD = 'mark27'
BASIC_AUTH_ENDPOINT = f'/basic-auth/{USERNAME}/{PASSWORD}'
BEARER_ENDPOINT = '/bearer'
BEARER_TOKEN = 'LAKSDLKASD'


class TestAuth:

    @pytest.mark.api
    def test_basic_auth(self, base_url):
        logging.info(f"Getting endpoint: {base_url + BASIC_AUTH_ENDPOINT}")
        basic_auth_response = requests.get(base_url + BASIC_AUTH_ENDPOINT, auth=(USERNAME, PASSWORD))
        assert basic_auth_response.status_code == 200
        assert basic_auth_response.json().get('authenticated') == True
        assert basic_auth_response.json().get('user') == USERNAME

    @pytest.mark.api
    def test_bearer_auth(self, base_url):
        logging.info(f"Getting endpoint: {base_url + BEARER_ENDPOINT}")
        headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
        bearer_auth_response = requests.get(base_url + BEARER_ENDPOINT, headers=headers)
        assert bearer_auth_response.status_code == 200
        assert bearer_auth_response.json().get('authenticated') == True
        assert bearer_auth_response.json().get('token') == BEARER_TOKEN
