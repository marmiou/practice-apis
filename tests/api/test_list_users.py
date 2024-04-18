import logging
import pytest
import requests

LIST_API = '/api/users'


class TestGetListUsers:
    @pytest.mark.api
    @pytest.mark.listUsers
    def test_list_users_should_return_success(self,base_reqres_url):
        url = base_reqres_url + LIST_API
        pages = {"page": 2}
        logging.info(f"Endpoint: {url}")
        response = requests.get(url, params=pages)
        logging.info(response.json().get('data')[0])
        assert response.status_code == 200, f"Response should have status 200, but got {response.status_code}"

    @pytest.mark.api
    @pytest.mark.listUsers
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


    @pytest.mark.api
    @pytest.mark.listUsers
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

        @pytest.mark.api
        @pytest.mark.listUsers
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

        @pytest.mark.api
        @pytest.mark.listUsers
        def test_list_users_data_integrity(base_reqres_url):
            url = base_reqres_url + LIST_API
            pages = {"page": 2}
            logging.info(f"Endpoint: {url}")
            response = requests.get(url, params=pages)
            response_data = response.json()
            ids = [user['id'] for user in response_data['data']]
            assert len(ids) == len(set(ids)), "IDs are not unique within the returned data"
            assert response_data['total'] == len(
                response_data['data']), "Total attribute is not consistent with the number of items returned"
            assert response_data['total_pages'] == 1 or response_data[
                'total_pages'] == 2, "Total pages attribute is not consistent with the data returned"

        @pytest.mark.api
        @pytest.mark.listUsers
        def test_list_users_pagination_first_page(base_reqres_url):
            url = base_reqres_url + LIST_API
            pages = {"page": 1}
            logging.info(f"Endpoint: {url}")
            response = requests.get(url, params=pages)
            response_data_first = response.json()
            assert response_data_first['page'] == 1, "First page request should return page 1"

        @pytest.mark.api
        @pytest.mark.listUsers
        def test_list_users_pagination_last_page(base_reqres_url):
            url = base_reqres_url + LIST_API
            pages = {"page": 2}
            logging.info(f"Endpoint: {url}")
            response = requests.get(url, params=pages)
            response_data_last = response.json()
            assert response_data_last['page'] == 2, "Last page request should return page 2"

        @pytest.mark.api
        @pytest.mark.listUsers
        def test_list_users_pagination_non_existing_page(base_reqres_url):
            # Requesting a page beyond the total number of pages
            url = base_reqres_url + LIST_API
            pages = {"page": 3}
            logging.info(f"Endpoint: {url}")
            response = requests.get(url, params=pages)
            assert response.status_code == 200, "Requesting a page beyond the total number of pages should still return status 200"
            assert response.json()[
                       'data'] == [], "Requesting a page beyond the total number of pages should return an empty data array"

