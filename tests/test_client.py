import unittest

from base64 import b64encode

from glovo_api_python import __version__
from glovo_api_python.client import Client
from glovo_api_python.constants import Stage


class ClientTest(unittest.TestCase):
    api_key = 'sample_api_key'
    api_secret = 'sample_api_secret'
    version = __version__

    def test_client_default_production_stage(self):
        client = Client(self.api_key, self.api_secret)

        assert client.stage == Stage.PRODUCTION
        assert client.base_url == 'https://api.glovoapp.com'

    def test_client_production_stage(self):
        client = Client(self.api_key, self.api_secret, stage=Stage.PRODUCTION)

        assert client.stage == Stage.PRODUCTION
        assert client.base_url == 'https://api.glovoapp.com'

    def test_client_test_stage(self):
        client = Client(self.api_key, self.api_secret, stage=Stage.TEST)

        assert client.stage == Stage.TEST
        assert client.base_url == 'https://stageapi.glovoapp.com'

    def test_client_stage_updates(self):
        client = Client(self.api_key, self.api_secret, stage=Stage.PRODUCTION)

        assert client.stage == Stage.PRODUCTION
        assert client.base_url == 'https://api.glovoapp.com'

        client.enable_test_mode()

        assert client.stage == Stage.TEST
        assert client.base_url == 'https://stageapi.glovoapp.com'

        client.disable_test_mode()

        assert client.stage == Stage.PRODUCTION
        assert client.base_url == 'https://api.glovoapp.com'

    def test_client_auth_string(self):
        client = Client(self.api_key, self.api_secret, stage=Stage.TEST)

        raw_auth_string = f'{self.api_key}:{self.api_secret}'.encode('utf-8')
        auth_string = b64encode(raw_auth_string).decode('utf-8')

        assert client.auth_string == auth_string

    def test_client_headers(self):
        client = Client(self.api_key, self.api_secret, stage=Stage.TEST)

        raw_auth_string = f'{self.api_key}:{self.api_secret}'.encode('utf-8')
        auth_string = b64encode(raw_auth_string).decode('utf-8')
        headers = {
            'User-Agent': f'Globo-API-Python/{self.version}',
            'Authorization': f'Basic {auth_string}',
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }

        assert headers['User-Agent'] == client.session.headers['User-Agent']
        assert headers['Authorization'] == client.session.headers['Authorization']
        assert headers['Content-type'] == client.session.headers['Content-type']
        assert headers['Accept'] == client.session.headers['Accept']


if __name__ == '__main__':
    unittest.main()
