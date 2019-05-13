import os
import unittest

from dotenv import load_dotenv

from glovo_api_python import __version__
from glovo_api_python.client import Client
from glovo_api_python.constants import Stage
from glovo_api_python.resources import WorkingArea


class WorkingAreasTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.api_key = os.environ.get('API_KEY', 'sample_api_key')
        self.api_secret = os.environ.get('API_SECRET', 'sample_api_secret')
        self.version = __version__
        self.client = Client(self.api_key, self.api_secret)
        # self.client.enable_test_mode()

    def test_working_area_attribute_type(self):
        working_area = getattr(self.client, 'working_area', None)

        assert isinstance(working_area, WorkingArea)

    def test_working_area_client(self):
        working_area = getattr(self.client, 'working_area', None)

        assert working_area.client == self.client

    def test_working_area_response_status_code(self):
        response = self.client.working_area.list()
        assert response['status'] == 200


if __name__ == '__main__':
    unittest.main()
