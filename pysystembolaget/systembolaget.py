"""Systembolaget."""
import http.client
import json
import urllib.parse

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

    def product_search(self, sort_direction=None, sort_by=None, page=None,
                       search_query=None, country=None, origin_level_1=None,
                       origin_level_2=None, origin_level_3=None, vintage=None,
                       sub_category=None, type=None, style=None,
                       assortment_text=None, bottle_type_group=None, seal=None,
                       grape=None, price_min=None, price_max=None,
                       alcohol_percentage_min=None,
                       alcohol_percentage_max=None,
                       news=None, csr=None, other_selections=None,
                       sell_start_date_from=None, sell_start_date_to=None):
        """API: Product_Search."""
        params = {}
        params['SortDirection'] = sort_direction
        params['SortBy'] = sort_by
        params['Page'] = page
        params['SearchQuery'] = search_query
        params['Country'] = country
        params['OriginLevel1'] = origin_level_1
        params['OriginLevel2'] = origin_level_2
        params['OriginLevel3'] = origin_level_3
        params['Vintage'] = vintage
        params['SubCategory'] = sub_category
        params['Type'] = type
        params['Style'] = style
        params['AssortmentText'] = assortment_text
        params['BottleTypeGroup'] = bottle_type_group
        params['Seal'] = seal
        params['Grape'] = grape
        params['PriceMin'] = price_min
        params['PriceMax'] = price_max
        params['AlcoholPercentageMin'] = alcohol_percentage_min
        params['AlcoholPercentageMax'] = alcohol_percentage_max
        params['News'] = news
        params['Csr'] = csr
        params['OtherSelections'] = other_selections
        params['SellStartDateFrom'] = sell_start_date_from
        params['SellStartDateTo'] = sell_start_date_to
        params = {key: value for key, value in params.items()
                  if value is not None}
        params = urllib.parse.urlencode(params)
        url = API_PRODUCT_URL + 'search?%s' % params
        return self.__GET__(url)
