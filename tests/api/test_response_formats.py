import logging
import requests
import pytest
import xml

DENY = '/deny'
XML = '/xml'
HTML = '/html'


class TestResponseFormats:
    @pytest.mark.api
    def test_get_deny_should_return_expected_data(self, base_url):
        url = base_url + DENY
        logging.info(f'Endpoint{url}')
        response = requests.get(url)
        assert response.status_code == 200
        error_message = response.text.lower()
        expected_error_message = (
            "          .-''''''-.\n"
            "        .' _      _ '.\n"
            "       /   o      o   \\\n"
            "      :                :\n"
            "      |                |\n"
            "      :       __       :\n"
            "       \\  .-\"`  `\"-.  /\n"
            "        '.          .'\n"
            "          '-......-'\n"
            "     you shouldn't be here"
        )
        assert expected_error_message in error_message, f"Expected error message not found in response: {error_message}"

    def test_get_xml_should_return_expected_data(self, base_url):
        url = base_url + XML
        logging.info(f'Endpoint: {url}')
        response = requests.get(url)
        logging.info(response)
        assert response.status_code == 200


