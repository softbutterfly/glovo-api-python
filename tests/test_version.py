import unittest

from glovo_api_python import __version__


class VersionTest(unittest.TestCase):
    @staticmethod
    def test_version():
        assert __version__ == "0.1.1"


if __name__ == "__main__":
    unittest.main()
