"""Init file for pysystembolaget."""
import requests

session = requests.Session()
session.headers = {}


def set_ocp_apim_subscription_key(ocp_apim_subscription_key):
    session.headers['Ocp-Apim-Subscription-Key'] = ocp_apim_subscription_key


from .product import Product  # noqa: E402

__all__ = ['Product']
