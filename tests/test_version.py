import unittest

from glovo_api_python import __version__


class VersionTest(unittest.TestCase):
    @staticmethod
    def test_version():
        assert __version__ == "2.0.0"


if __name__ == "__main__":
    unittest.main()
