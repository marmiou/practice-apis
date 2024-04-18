import logging
import pytest
import requests

LIST_API = '/api/users'

class TestCrudUsers:
    @pytest.mark.api
    @pytest.mark.users
    def test_list_users_should_return_success(self,base_reqres_url):
        url = base_reqres_url + LIST_API
        pages = {"page": 2}
        logging.info(f"Endpoint: {url}")
        response = requests.get(url, params=pages)
        logging.info(response.json().get('data')[0])
        assert response.status_code == 200, f"Response should have status 200, but got {response.status_code}"

    def test_list_users_response_should_contain_all_attributes(self, base_reqres_url):
        url = base_reqres_url + LIST_API
        pages = {"page": 2}
        logging.info(f"Endpoint: {url}")
        response = requests.get(url, params=pages)
        logging.info(response.json().get('data')[0])
        assert 'page' in response.json(), "Attribute page is missing"
        assert 'per_page' in response.json(), "Attribute 'per_page' is missing"
        assert 'total' in response.json(), "Attribute 'total' is missing"
        assert 'total_pages' in response.json(), "Attribute 'total_pages' is missing"
        assert 'data' in response.json(), "Attribute 'data' is missing"
        assert 'support' in response.json(), "Attribute 'support' is missing"

    def test_list_users_response_should_contain_correct_values(self, base_reqres_url):
        url = base_reqres_url + LIST_API
        pages = {"page": 2}
        logging.info(f"Endpoint: {url}")
        response = requests.get(url, params=pages)
        response_data = response.json()
        assert response_data.get('page') == pages.get(
            'page'), f"Attribute 'page' should have value {pages.get('page')}, but got {response_data.get('page')}"
        assert response_data.get('per_page') == 6, "Attribute 'per_page' should have value 6"
        assert response_data.get('total') == 12, "Attribute 'total' should have value 12"
        assert response_data.get('total_pages') == 2, "Attribute 'total_pages' should have value 2"
        assert len(response_data.get('data')) == 6, "Length of 'data' array should be 6"

        def test_list_users_response_headers(base_reqres_url):
            url = base_reqres_url + LIST_API
            pages = {"page": 2}
            logging.info(f"Endpoint: {url}")
            response = requests.get(url, params=pages)
            assert 'content-type' in response.headers, "Content-Type header is missing"
            assert response.headers[
                       'content-type'] == 'application/json; charset=utf-8', "Content-Type header should be 'application/json; charset=utf-8'"
            assert 'cache-control' in response.headers, "Cache-Control header is missing"
            assert 'x-powered-by' in response.headers, "X-Powered-By header is missing"

        
    # @pytest.mark.api
    # @pytest.mark.users
