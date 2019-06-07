"""Test Systembolaget Product API."""
import pytest
import vcr

import pysystembolaget


@pytest.fixture
def product_properties():
    """List of all product properties."""
    return ['ProductId', 'ProductNumber', 'ProductNameBold', 'ProductNameThin',
            'Category', 'ProductNumberShort', 'ProducerName', 'SupplierName',
            'IsKosher', 'BottleTextShort', 'Seal', 'RestrictedParcelQuantity',
            'IsOrganic', 'IsEthical', 'EthicalLabel', 'IsWebLaunch',
            'SellStartDate', 'IsCompletelyOutOfStock', 'IsTemporaryOutOfStock',
            'AlcoholPercentage', 'Volume', 'Price', 'Country', 'OriginLevel1',
            'OriginLevel2', 'Vintage', 'SubCategory', 'Type', 'Style',
            'AssortmentText', 'BeverageDescriptionShort', 'Usage', 'Taste',
            'Assortment', 'RecycleFee', 'IsManufacturingCountry',
            'IsRegionalRestricted', 'IsInStoreSearchAssortment', 'IsNews']


@vcr.use_cassette('tests/vcr_cassettes/product-get.yaml',
                  filter_headers=['Ocp-Apim-Subscription-Key'])
def test_product_get(product_properties):
    """Test product get."""
    response = pysystembolaget.Product.get(508314)

    assert isinstance(response, dict)
    assert response['ProductId'] == '508314'
    assert set(product_properties).issubset(response.keys())


@vcr.use_cassette('tests/vcr_cassettes/product-get-all-products.yaml',
                  filter_headers=['Ocp-Apim-Subscription-Key'])
def test_product_get_all_prodcuts(product_properties):
    """Test product get all products."""
    response = pysystembolaget.Product.get_all_products()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(product_properties).issubset(response[0].keys())


@vcr.use_cassette('tests/vcr_cassettes/product-get-products-with-store.yaml',
                  filter_headers=['Ocp-Apim-Subscription-Key'])
def test_product_get_products_with_store():
    """Test product get products with store."""
    response = pysystembolaget.Product.get_products_with_store()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(['SiteId', 'Products']).issubset(response[0].keys())
    products = response[0]['Products']
    assert isinstance(products, list)
    assert isinstance(products[0], dict)
    assert set(['ProductId', 'ProductNumber']).issubset(products[0].keys())
