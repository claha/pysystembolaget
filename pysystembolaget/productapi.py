"""Systembolaget Product API."""
import http.client
import json

from .const import API_HOST, API_KEY_HEADER, API_PRODUCT_URL


class ProductAPI():
    """Product API."""

    def __init__(self, api_key):
        """Initialize ProductAPI."""
        self._headers = {
            API_KEY_HEADER: api_key
        }

    def __GET__(self, url):
        """Get request towards prudct api."""
        conn = http.client.HTTPSConnection(API_HOST)
        method = 'GET'
        conn.request(method,
                     url,
                     body="{body}",
                     headers=self._headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()

        return json.loads(data)

    def get(self, product_id):
        """Get."""
        url = API_PRODUCT_URL + str(product_id)
        return self.__GET__(url)

    def get_all_products(self):
        """Get all products."""
        url = API_PRODUCT_URL
        return self.__GET__(url)

    def get_products_with_store(self):
        """Get products with store."""
        url = API_PRODUCT_URL + 'getproductswithstore'
        return self.__GET__(url)
