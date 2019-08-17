"""Systembolaget Product API."""
from .const import API_PRODUCT_URL, API_KEY_HEADER

import requests


class ProductAPI():
    """Product API."""

    def __init__(self, api_key):
        """Initialize ProductAPI."""
        self._session = requests.Session()
        self._session.headers = {}
        self._session.headers[API_KEY_HEADER] = api_key

    def get(self, product_id):
        """Get."""
        url = API_PRODUCT_URL + str(product_id)
        response = self._session.get(url)
        return response.json()

    def get_all_products(self):
        """Get all products."""
        url = API_PRODUCT_URL
        response = self._session.get(url)
        return response.json()

    def get_products_with_store(self):
        """Get products with store."""
        url = API_PRODUCT_URL + 'getproductswithstore'
        response = self._session.get(url)
        return response.json()
