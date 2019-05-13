import unittest

from glovo_api_python import __version__


class VersionTest(unittest.TestCase):
    def test_version(self):
        assert __version__ == '0.1.0'
