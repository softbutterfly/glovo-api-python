import json
import os
import unittest

import pytest
from dotenv import load_dotenv

from glovo_api_python import __version__
from glovo_api_python.client import Glovo
from glovo_api_python.resources import Order


class OrdersTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.version = __version__

        self.api_key = os.environ.get("API_KEY", "sample_api_key")
        self.api_secret = os.environ.get("API_SECRET", "sample_api_secret")
        self.order_id = os.environ.get("ORDER_ID", "sample_order_id")
        self.order_to_estimate = os.environ.get("ORDER_TO_ESTIMATE", "{}")
        self.order_to_estimate = json.loads(self.order_to_estimate)

        self.client = Glovo(self.api_key, self.api_secret)
        if bool(os.environ.get("TEST", False)):
            self.client.enable_test_mode()
        self.order = Order(client=self.client)

    def test_order_attribute_type(self):
        order = getattr(self.client, "order", None)
        assert isinstance(order, Order)

    def test_order_client(self):
        order = getattr(self.client, "order", None)

        assert order.client == self.client

    @pytest.mark.vcr()
    def test_order_list_status_code(self):
        response = self.order.list()

        assert response["status"] == 200

    @pytest.mark.vcr()
    def test_order_read_status_code(self):
        response = self.order.read(self.order_id)
        assert response["status"] == 200

    @pytest.mark.vcr()
    def test_order_estimate_status_code(self):
        response = self.order.estimate(self.order_to_estimate)
        assert response["status"] == 200

    # @pytest.mark.vcr()
    # def test_order_create_status_code(self):
    #     response = self.order.create(self.order_to_estimate)
    #     assert response["status"] == 200


if __name__ == "__main__":
    unittest.main()
