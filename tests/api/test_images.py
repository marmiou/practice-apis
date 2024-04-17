import logging

import cairosvg
import pytest
import requests
from PIL import Image
from io import BytesIO


JPEG = '/image/jpeg'
PNG = '/image/png'
SVG = '/image/svg'
webp = '/image/webp'


# In those types of test we check 3 different assertions:
# 1. Status code OK
# 2. Content type is the respective one
# 3. Image integrity
class TestImages:

    @pytest.mark.api
    @pytest.mark.images
    def test_jpeg_image(self, base_url):
        url = base_url + JPEG
        logging.info(f'Getting jpeg image via: {url}')
        response = requests.get(url)
        assert response.status_code == 200
        content_type = response.headers.get('Content-Type')
        assert content_type == 'image/jpeg', f"Expected content type image/jpeg, but got {content_type}"

        try:
            Image.open(BytesIO(response.content))
        except Exception as e:
            assert False, f"Failed to open image: {e}"

    @pytest.mark.api
    @pytest.mark.images
    def test_png_image(self, base_url):
        url = base_url + PNG
        logging.info(f'Getting PNG image via: {url}')
        response = requests.get(url)

        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        content_type = response.headers.get('Content-Type')
        assert content_type == 'image/png', f"Expected content type 'image/png', but got {content_type}"

        try:
            Image.open(BytesIO(response.content))
        except Exception as e:
            assert False, f"Failed to open image: {e}"

    @pytest.mark.api
    @pytest.mark.images
    def test_svg_image(self, base_url):
        url = base_url + SVG
        logging.info(f'Getting SVG image via: {url}')
        response = requests.get(url)

        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        content_type = response.headers.get('Content-Type')
        assert content_type == 'image/svg+xml', f"Expected content type 'image/svg+xml', but got {content_type}"

        png_image = cairosvg.svg2png(response.content)
        try:
            Image.open(BytesIO(png_image))
        except Exception as e:
            assert False, f"Failed to open image: {e}"

    @pytest.mark.xfail(reason="Test is expected to fail: The content type in the actual response header is svg+xml")
    @pytest.mark.images
    def test_webp_image(self, base_url):
        url = base_url + SVG
        logging.info(f'Getting WEBP image via: {url}')
        response = requests.get(url)

        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        content_type = response.headers.get('Content-Type')
        assert content_type == 'image/webp', f"Expected content type 'image/webp', but got {content_type}"

        try:
            Image.open(BytesIO(response.content))
        except Exception as e:
            assert False, f"Failed to open image: {e}"