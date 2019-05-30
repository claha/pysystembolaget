"""Systembolaget Product."""
from . import session


class Product():
    """Representaion of a product."""

    def __init__(self, product_id):
        """Initialize a product."""
        self._product_id = product_id

    def properties(self):
        """Retireve properties of a product."""
        url = 'https://api-extern.systembolaget.se/product/v1/product/{}'
        url = url.format(self._product_id)
        response = session.get(url)
        return response.json()
