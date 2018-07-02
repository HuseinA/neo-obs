from .requestors import CloudianRequestor


class User(object):
    base_url = 'user'

    def __init__(self, requestor):
        self.requestor = requestor

    def list(self, data=None, json=None, method='GET'):
        base_url = self.base_url + '/list'
        list_user = CloudianRequestor.request(self.requestor,
                                              url=base_url,
                                              data=data,
                                              json=json,
                                              method=method)

        return list_user

    def get(self, data=None, json=None, method='GET'):
        get_user = CloudianRequestor.request(self.requestor,
                                             url=self.base_url,
                                             data=data,
                                             json=json,
                                             method=method)

        return get_user
