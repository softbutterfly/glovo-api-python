from ..constants.urls import URL
from .base import Resource


class Order(Resource):
    endpoint = URL.ORDER

    def estimate(self, data=None, **options):
        path = "{0}/estimate".format(self.endpoint)
        return self._post(path, data, **options)

    def tracking(self, id_, data=None, **options):
        path = "{0}/{1}/tracking".format(self.endpoint, id_)
        return self._get(path, data, **options)

    def glover_info(self, id_, data=None, **options):
        path = "{0}/{1}/courier-contact".format(self.endpoint, id_)
        return self._get(path, data, **options)

    def cancel(self, id_, data=None, **options):
        path = "{0}/{1}/cancel".format(self.endpoint, id_)
        return self._post(path, data, **options)
