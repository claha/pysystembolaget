"""Configure tests."""
import pytest

import pysystembolaget


def pytest_addoption(parser):
    """Add commandline options."""
    parser.addoption(
        '--key', help="Ocp-Apim-Subscription-Key", type=str, default=''
    )


@pytest.fixture(scope='session', autouse=True)
def session_fixture(request):
    """Run before each test session."""
    key = request.config.getoption('--key')
    pysystembolaget.set_ocp_apim_subscription_key(key)
