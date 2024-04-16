import logging

import pytest
import requests



RANDOM_ENDPOINT = "/facts/random"
FACTS_ENDPOINT = "/facts/"


class TestClass:

    @pytest.mark.api
    def test_check(self, base_url):
        get_facts_response = requests.get(base_url + FACTS_ENDPOINT)
        assert get_facts_response.status_code == 200

