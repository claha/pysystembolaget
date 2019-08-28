"""Test Systembolaget Product."""
import pytest
import vcr


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


class TestSystembolagetProduct():
    """Test Systembolaget Product."""

    @vcr.use_cassette(
        'tests/vcr_cassettes/product-get.yaml',
        filter_headers=['Ocp-Apim-Subscription-Key'])
    def test_product_get(self, product_properties):
        """Test product get."""
        response = self.systembolaget.product_get(508314)

        assert isinstance(response, dict)
        assert response['ProductId'] == '508314'
        assert set(product_properties).issubset(response.keys())

    @vcr.use_cassette(
        'tests/vcr_cassettes/product-get-all-products.yaml',
        filter_headers=['Ocp-Apim-Subscription-Key'])
    def test_product_get_all_prodcuts(self, product_properties):
        """Test product get all products."""
        response = self.systembolaget.product_get_all_products()

        assert isinstance(response, list)
        assert isinstance(response[0], dict)
        assert set(product_properties).issubset(response[0].keys())

    @vcr.use_cassette(
        'tests/vcr_cassettes/product-get-products-with-store.yaml',
        filter_headers=['Ocp-Apim-Subscription-Key'])
    def test_product_get_products_with_store(self):
        """Test product get products with store."""
        response = self.systembolaget.product_get_products_with_store()

        assert isinstance(response, list)
        assert isinstance(response[0], dict)
        assert set(['SiteId', 'Products']).issubset(response[0].keys())
        products = response[0]['Products']
        assert isinstance(products, list)
        assert isinstance(products[0], dict)
        assert set(['ProductId', 'ProductNumber']).issubset(products[0].keys())

    @vcr.use_cassette(
        'tests/vcr_cassettes/product-search.yaml',
        filter_headers=['Ocp-Apim-Subscription-Key'])
    def test_product_search(self, product_properties):
        """Test product search."""
        response = self.systembolaget.product_search()

        assert isinstance(response, dict)
        assert isinstance(response['Hits'], list)
        assert isinstance(response['Metadata'], dict)
        assert set(['DocCount', 'NextPage', 'PriceRange']).issubset(
            response['Metadata'].keys())
        assert isinstance(response['Hits'][0], dict)
        assert set(product_properties).issubset(response['Hits'][0].keys())
