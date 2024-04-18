import logging

import pytest
import requests

USERNAME = "mark"
PASSWORD = "mark27"
BASIC_AUTH_ENDPOINT = f"/basic-auth/{USERNAME}/{PASSWORD}"
BEARER_ENDPOINT = "/bearer"
BEARER_TOKEN = "LAKSDLKASD"
HIDDEN_BASIC_AUTH_ENDPOINT = f"/hidden-basic-auth/{USERNAME}/{PASSWORD}"


class TestAuth:

    @pytest.mark.api
    # Note: The implementation of basic auth should not include username and password in the endpoint path according
    # to standards. However, httpbin requires it so the user can specify their own credentials.
    def test_basic_auth(self, base_httpbin_url):
        url = base_httpbin_url + BASIC_AUTH_ENDPOINT
        logging.info(f"Getting endpoint: {url}")
        response = requests.get(url, auth=(USERNAME, PASSWORD))
        assert response.status_code == 200
        assert response.json().get("authenticated") == True
        assert response.json().get("user") == USERNAME
        assert "Content-Type" in response.headers
        assert "Server" in response.headers

    @pytest.mark.api
    def test_bearer_auth(self, base_httpbin_url):
        url = base_httpbin_url + BEARER_ENDPOINT
        logging.info(f"Getting endpoint: {url}")
        headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
        response = requests.get(url, headers=headers)

        assert response.status_code == 200
        assert response.json().get("authenticated") == True
        assert response.json().get("token") == BEARER_TOKEN
        assert "Content-Type" in response.headers
        assert "Server" in response.headers

    @pytest.mark.api
    def test_hidden_basic_auth(self, base_httpbin_url):
        url = base_httpbin_url + HIDDEN_BASIC_AUTH_ENDPOINT
        logging.info(f"Getting endpoint: {url}")
        response = requests.get(url, auth=(USERNAME, PASSWORD))

        assert response.status_code == 200
        assert response.json().get("authenticated") == True
        assert response.json().get("user") == USERNAME
        assert "Content-Type" in response.headers
        assert "Server" in response.headers
