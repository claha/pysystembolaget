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
        if sort_direction:
            params['SortDirection'] = sort_direction
        if sort_by:
            params['SortBy'] = sort_by
        if page:
            params['Page'] = page
        if search_query:
            params['SearchQuery'] = search_query
        if country:
            params['Country'] = country
        if origin_level_1:
            params['OriginLevel1'] = origin_level_1
        if origin_level_2:
            params['OriginLevel2'] = origin_level_2
        if origin_level_3:
            params['OriginLevel3'] = origin_level_3
        if vintage:
            params['Vintage'] = vintage
        if sub_category:
            params['SubCategory'] = sub_category
        if type:
            params['Type'] = type
        if style:
            params['Style'] = style
        if assortment_text:
            params['AssortmentText'] = assortment_text
        if bottle_type_group:
            params['BottleTypeGroup'] = bottle_type_group
        if seal:
            params['Seal'] = seal
        if grape:
            params['Grape'] = grape
        if price_min:
            params['PriceMin'] = price_min
        if price_max:
            params['PriceMax'] = price_max
        if alcohol_percentage_min:
            params['AlcoholPercentageMin'] = alcohol_percentage_min
        if alcohol_percentage_max:
            params['AlcoholPercentageMax'] = alcohol_percentage_max
        if news:
            params['News'] = news
        if csr:
            params['Csr'] = csr
        if other_selections:
            params['OtherSelections'] = other_selections
        if sell_start_date_from:
            params['SellStartDateFrom'] = sell_start_date_from
        if sell_start_date_to:
            params['SellStartDateTo'] = sell_start_date_to
        params = urllib.parse.urlencode(params)
        url = API_PRODUCT_URL + 'search?%s' % params
        return self.__GET__(url)
