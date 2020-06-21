import json
from base64 import b64encode
from types import ModuleType

from requests import session

from . import resources
from .constants import URL, Stage
from .utils import capitalize_camel_case
from .version import VERSION

RESOURCE_PREFIX = "_resource_"
RESOURCE_CLASSES = {}

for name, module in resources.__dict__.items():
    capitalized_name = capitalize_camel_case(name)
    is_module = isinstance(module, ModuleType)
    is_in_module = capitalized_name in getattr(module, "__dict__", {})

    if is_module and is_in_module:
        RESOURCE_CLASSES[name] = module.__dict__[capitalized_name]


class Glovo:
    base_url = None

    def __init__(self, api_key, api_secret, stage=Stage.PRODUCTION):
        """Initialize a Glovo client object with session.

        Also includes optional auth handler and options.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.stage = stage
        self.session = session()

        self._set_auth_string()
        self._set_client_headers()
        self._set_base_url()

        for name, klass in RESOURCE_CLASSES.items():
            setattr(self, RESOURCE_PREFIX + name, klass(self))

    @staticmethod
    def _get_version():
        return ".".join(VERSION)

    @staticmethod
    def _update_request(data, options):
        """Update The resource data and header options."""
        data = json.dumps(data)

        if "headers" not in options:
            options["headers"] = {}

        options["headers"].update({"Content-type": "application/json"})

        return data, options

    def _set_auth_string(self):
        raw_auth_string = "{0}:{1}".format(self.api_key, self.api_secret).encode(
            "utf-8"
        )
        self.auth_string = b64encode(raw_auth_string).decode("utf-8")

    def _set_client_headers(self):
        self.session.headers.update(
            {
                "User-Agent": "Globo-API-Python/{0}".format(self._get_version()),
                "Authorization": "Basic {0}".format(self.auth_string),
                "Content-type": "application/json",
                "Accept": "application/json",
            }
        )

    def _set_base_url(self):
        prefix = URL.PREFIX[self.stage]
        self.base_url = URL.BASE_FORMAT.format(prefix=prefix)

    def _set_stage(self, stage):
        self.stage = stage
        self._set_base_url()

    def enable_test_mode(self):
        self._set_stage(Stage.TEST)

    def disable_test_mode(self):
        self._set_stage(Stage.PRODUCTION)

    def request(self, method, path, **options):
        """Dispatch a request to the Glovo HTTP API."""
        url = "{}{}".format(self.base_url, path)
        response = getattr(self.session, method)(url, **options)
        json_response = response.json()

        return {"status": response.status_code, "data": json_response}

    def get(self, path, params, **options):
        """Parse GET request options and dispatches a request."""
        return self.request("get", path, params=params, **options)

    # PATCH method is never used on Glovo resources
    # def patch(self, path, data, **options):
    #     """Parse PATCH request options and dispatches a request."""
    #     data, options = self._update_request(data, options)
    #     return self.request("patch", path, data=data, **options)

    def post(self, path, data, **options):
        """Parse POST request options and dispatches a request."""
        data, options = self._update_request(data, options)
        return self.request("post", path, data=data, **options)

    # DELETE method is never used on Glovo resources
    # def delete(self, path, data, **options):
    #     """Parse DELETE request options and dispatches a request."""
    #     data, options = self._update_request(data, options)
    #     return self.request("delete", path, data=data, **options)

    # PUT method is never used on Glovo resources
    # def put(self, path, data, **options):
    #     """Parse PUT request options and dispatches a request."""
    #     data, options = self._update_request(data, options)
    #     return self.request("put", path, data=data, **options)

    def __getattr__(self, name):
        # This method will be called if the standar accesos for a property
        # named `name` fails. I this situation if the propery name not start
        # with `RESOURCE_PREFIX` ...
        if not name.startswith(RESOURCE_PREFIX):
            # ... we will try to get the prefixed version of the attribute
            # name
            return getattr(self, RESOURCE_PREFIX + name)

        return super(Glovo, self).__getattribute__(name)
