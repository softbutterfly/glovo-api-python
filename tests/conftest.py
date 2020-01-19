import pytest


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("Authorization", "Bearer glovo_api_key")],
    }
