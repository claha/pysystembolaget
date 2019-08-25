"""Systembolaget."""
import http.client
import json

from .const import API_HOST, API_KEY_HEADER, API_PRODUCT_URL


class Systembolaget():
    """Systembolaget."""

    def __init__(self, api_key):
        """Initialize ProductAPI."""
        self._headers = {
            API_KEY_HEADER: api_key
        }

    def __GET__(self, url):
        """Get request towards systembolaget api."""
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

    def product_get(self, product_id):
        """API: Product_Get."""
        url = API_PRODUCT_URL + str(product_id)
        return self.__GET__(url)

    def product_get_all_products(self):
        """API: Product_GetAllProducts."""
        url = API_PRODUCT_URL
        return self.__GET__(url)

    def product_get_products_with_store(self):
        """API: Product_GetProductsWithStore."""
        url = API_PRODUCT_URL + 'getproductswithstore'
        return self.__GET__(url)
