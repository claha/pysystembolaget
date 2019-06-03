"""Systembolaget Product."""
from . import session


class Product():
    """Representaion of a product."""

    BASE_URL = 'https://api-extern.systembolaget.se/product/v1/product/'

    @classmethod
    def get(cls, product_id):
        """Get a product."""
        url = cls.BASE_URL + '{}'
        url = url.format(product_id)
        response = session.get(url)
        return response.json()

    @classmethod
    def get_all_products(cls):
        """Get all products."""
        url = cls.BASE_URL
        response = session.get(url)
        return response.json()
