"""Systembolaget Product API."""
from . import session
from .const import API_PRODUCT_URL


class Product():
    """Product API."""

    @classmethod
    def get(cls, product_id):
        """Get."""
        url = API_PRODUCT_URL + str(product_id)
        response = session.get(url)
        return response.json()

    @classmethod
    def get_all_products(cls):
        """Get all products."""
        url = API_PRODUCT_URL
        response = session.get(url)
        return response.json()

    @classmethod
    def get_products_with_store(cls):
        """Get products with store."""
        url = API_PRODUCT_URL + 'getproductswithstore'
        response = session.get(url)
        return response.json()
