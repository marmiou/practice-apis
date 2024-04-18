import logging

import pytest
import requests

GET_ENDPOINT = "/get"
PATCH_ENDPOINT = "/patch"
POST_ENDPOINT = "/post"
PUT_ENDPOINT = "/put"
DELETE_ENDPOINT = "/delete"


class TestHTTPMethods:

    @pytest.mark.api
    def test_get_should_return_success(self, base_httpbin_url):
        get_response = requests.get(base_httpbin_url + GET_ENDPOINT)
        logging.info(f"Got Get response: {get_response.json()}")
        assert get_response.status_code == 200

    @pytest.mark.api
    def test_patch_should_return_success(self, base_httpbin_url):
        patch_response = requests.patch(base_httpbin_url + PATCH_ENDPOINT)
        logging.info(f"Got patch response: {patch_response.json()}")
        assert patch_response.status_code == 200

    @pytest.mark.api
    def test_put_should_return_success(self, base_httpbin_url):
        put_response = requests.put(base_httpbin_url + PUT_ENDPOINT)
        logging.info(f"Got put response: {put_response.json()}")
        assert put_response.status_code == 200

    @pytest.mark.api
    def test_post_should_return_success(self, base_httpbin_url):
        post_response = requests.post(base_httpbin_url + POST_ENDPOINT)
        logging.info(f"Got post response: {post_response.json()}")
        assert post_response.status_code == 200

    @pytest.mark.api
    def test_delete_should_return_success(self, base_httpbin_url):
        delete_response = requests.delete(base_httpbin_url + DELETE_ENDPOINT)
        logging.info(f"Got delete response: {delete_response.json()}")
        assert delete_response.status_code == 200
