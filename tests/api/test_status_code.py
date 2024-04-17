import logging

import pytest
import requests

STATUS_ENDPOINT = "/status/"


# Just a documentation of most common 2xx, 4xx and 5xx status codes. If the response contained error, it would be nice
# to check the error message in the following tests to ensure it is the correct one. Also, in real case scenarios, we
# try to find ways in order to reproduce those responses with real endpoints
class TestStatusCodes:

    # 2xx Success
    @pytest.mark.api
    def test_delete_status_code_should_return_success_ok(self, base_url):
        codes = 200
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    @pytest.mark.api
    def test_delete_status_code_should_return_success_created(self, base_url):
        codes = 201
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    @pytest.mark.api
    def test_delete_status_code_should_return_success_accepted(self, base_url):
        codes = 202
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    @pytest.mark.api
    def test_delete_status_code_should_return_success_no_content(self, base_url):
        codes = 204
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    @pytest.mark.api
    def test_delete_status_code_should_return_redirect(self, base_url):
        codes = 300
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    # Client error codes
    @pytest.mark.api
    def test_delete_status_code_should_return_bad_request(self, base_url):
        codes = 400
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    @pytest.mark.api
    def test_delete_status_code_should_return_unauthorized(self, base_url):
        codes = 401
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    @pytest.mark.api
    def test_delete_status_code_should_return_payment_required(self, base_url):
        codes = 402
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    @pytest.mark.api
    def test_delete_status_code_should_return_forbidden(self, base_url):
        codes = 403
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    def test_delete_status_code_should_return_not_found(self, base_url):
        codes = 404
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    def test_delete_status_code_should_return_method_not_allowed(self, base_url):
        codes = 405
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    def test_delete_status_code_should_return_not_acceptable(self, base_url):
        codes = 406
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    def test_delete_status_code_should_return_proxy_auth_required(self, base_url):
        codes = 407
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    def test_delete_status_code_should_return_request_timeout(self, base_url):
        codes = 408
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    def test_delete_status_code_should_return_conflict(self, base_url):
        codes = 409
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    def test_delete_status_code_should_return_unsupported_media_type(self, base_url):
        codes = 415
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    # Server Error Codes
    def test_delete_status_code_should_return_internal_server_error(self, base_url):
        codes = 500
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    def test_delete_status_code_should_return__not_implemented(self, base_url):
        codes = 501
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    def test_delete_status_code_should_return_bad_gateway(self, base_url):
        codes = 502
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    def test_delete_status_code_should_return_service_unavailable(self, base_url):
        codes = 503
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    def test_delete_status_code_should_return_gateway_timeout(self, base_url):
        codes = 504
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    def test_delete_status_code_should_return_version_not_supported(self, base_url):
        codes = 505
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes

    def test_delete_status_code_should_return_insufficient_storage(self, base_url):
        codes = 507
        url = f"{base_url}{STATUS_ENDPOINT}{codes}"
        logging.info(f"Endpoint: {url}")
        response = requests.delete(url)
        assert response.status_code == codes
