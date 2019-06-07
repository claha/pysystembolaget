"""Systembolaget Product API."""
from . import session


class Product():
    """Product API."""

    BASE_URL = 'https://api-extern.systembolaget.se/product/v1/product/'

    @classmethod
    def get(cls, product_id):
        """Get."""
        url = cls.BASE_URL + str(product_id)
        response = session.get(url)
        return response.json()

    @classmethod
    def get_all_products(cls):
        """Get all products."""
        url = cls.BASE_URL
        response = session.get(url)
        return response.json()

    @classmethod
    def get_products_with_store(cls):
        """Get products with store."""
        url = cls.BASE_URL + 'getproductswithstore'
        response = session.get(url)
        return response.json()
