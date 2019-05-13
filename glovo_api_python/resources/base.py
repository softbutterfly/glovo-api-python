class Resource:
    endpoint = None

    def __init__(self, client=None):
        self.client = client

    def _get(self, path, data, **kwargs):
        return self.client.get(path, data, **kwargs)

    def _patch(self, path, data, **kwargs):
        return self.client.patch(path, data, **kwargs)

    def _post(self, path, data, **kwargs):
        return self.client.post(path, data, **kwargs)

    def _put(self, path, data, **kwargs):
        return self.client.put(path, data, **kwargs)

    def _delete(self, path, data, **kwargs):
        return self.client.delete(path, data, **kwargs)

    def create(self, data, **options):
        path = self.endpoint
        return self._post(path, data, **options)

    def list(self, data=None, **options):
        path = self.endpoint
        return self._get(path, data, **options)

    def read(self, id_, data=None, **options):
        path = f'{self.endpoint}/{id_}'
        return self._get(path, data, **options)

    def update(self, id_, data=None, **options):
        path = f'{self.endpoint}/{id_}'
        return self._put(path, data, **options)

    def delete(self, id_, data=None, **options):
        path = f'{self.endpoint}/{id_}'
        return self.delete(path, data, **options)
