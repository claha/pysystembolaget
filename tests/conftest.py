"""Configure tests."""
import pytest

import pysystembolaget


def pytest_addoption(parser):
    """Add commandline options."""
    parser.addoption(
        '--api_key', help="Ocp-Apim-Subscription-Key", type=str, default=''
    )


@pytest.fixture(scope='class', autouse=True)
def class_fixture(request):
    """Run before each test class."""
    api_key = request.config.getoption('--api_key')
    request.cls.api = pysystembolaget.ProductAPI(api_key)
