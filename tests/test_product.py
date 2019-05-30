"""Test pysystembolaget Product."""
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


@vcr.use_cassette('tests/vcr_cassettes/product-properties.yaml',
                  filter_headers=['Ocp-Apim-Subscription-Key'])
def test_product_properties(product_properties):
    """Test product properties."""
    product = pysystembolaget.Product(508314)
    response = product.properties()

    assert isinstance(response, dict)
    assert response['ProductId'] == '508314'
    assert set(product_properties).issubset(response.keys())
