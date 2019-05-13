from .base import Resource
from ..constants.urls import URL


class Order(Resource):
    endpoint = URL.ORDER

    def estimate(self, data=None, **options):
        path = f'{self.endpoint}/estimate'
        return self._post(path, data, **options)

    def tracking(self, id_, data=None, **options):
        path = f'{self.endpoint}/{id_}/tracking'
        return self._get(path, data, **options)

    def courier_contact(self, id_, data=None, **options):
        path = f'{self.endpoint}/{id_}/courier-contact'
        return self._get(path, data, **options)

    def cancel(self, id_, data=None, **options):
        path = f'{self.endpoint}/{id_}/cancel'
        return self._post(path, data, **options)
