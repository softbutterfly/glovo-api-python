import unittest
from base64 import b64encode

import pytest

from glovo_api_python import __version__
from glovo_api_python.client import RESOURCE_PREFIX, Glovo
from glovo_api_python.constants import Stage


class ClientTest(unittest.TestCase):
    # The following api credentials are not used in any security context.
    # It is only used to generate a sample client for basic functionalitiy
    # testing.
    api_key = "sample_api_key"  # nosec
    api_secret = "sample_api_secret"  # nosec
    version = __version__

    def _get_auth_string(self):
        raw_auth_string = "{0}:{1}".format(self.api_key, self.api_secret).encode(
            "utf-8"
        )
        return b64encode(raw_auth_string).decode("utf-8")

    def test_client_default_production_stage(self):
        client = Glovo(self.api_key, self.api_secret)

        assert client.stage == Stage.PRODUCTION
        assert client.base_url == "https://api.glovoapp.com"

    def test_client_production_stage(self):
        client = Glovo(self.api_key, self.api_secret, stage=Stage.PRODUCTION)

        assert client.stage == Stage.PRODUCTION
        assert client.base_url == "https://api.glovoapp.com"

    def test_client_test_stage(self):
        client = Glovo(self.api_key, self.api_secret, stage=Stage.TEST)

        assert client.stage == Stage.TEST
        assert client.base_url == "https://stageapi.glovoapp.com"

    def test_client_stage_updates(self):
        client = Glovo(self.api_key, self.api_secret, stage=Stage.PRODUCTION)

        assert client.stage == Stage.PRODUCTION
        assert client.base_url == "https://api.glovoapp.com"

        client.enable_test_mode()

        assert client.stage == Stage.TEST
        assert client.base_url == "https://stageapi.glovoapp.com"

        client.disable_test_mode()

        assert client.stage == Stage.PRODUCTION
        assert client.base_url == "https://api.glovoapp.com"

    def test_client_auth_string(self):
        client = Glovo(self.api_key, self.api_secret, stage=Stage.TEST)
        auth_string = self._get_auth_string()
        assert client.auth_string == auth_string

    def test_client_headers(self):
        client = Glovo(self.api_key, self.api_secret, stage=Stage.TEST)
        auth_string = self._get_auth_string()

        headers = {
            "User-Agent": "Globo-API-Python/{}".format(self.version),
            "Authorization": "Basic {}".format(auth_string),
            "Content-type": "application/json",
            "Accept": "application/json",
        }

        assert headers["User-Agent"] == client.session.headers["User-Agent"]
        assert headers["Authorization"] == client.session.headers["Authorization"]
        assert headers["Content-type"] == client.session.headers["Content-type"]
        assert headers["Accept"] == client.session.headers["Accept"]

    def test_non_injected_property(self):
        client = Glovo(self.api_key, self.api_secret, stage=Stage.TEST)
        attribute_name = "dummy_attribute"
        message = (
            "'Glovo' object has no attribute '%sdummy_attribute'" % RESOURCE_PREFIX
        )

        with pytest.raises(AttributeError) as excinfo:
            getattr(client, attribute_name)

        assert message in str(excinfo.value)


if __name__ == "__main__":
    unittest.main()
