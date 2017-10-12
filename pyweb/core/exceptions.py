from pyweb.exceptions.base import PyWebException

class EndpointAlreadyRegistered(PyWebException):

    def __init__(self, http_request):
        msg = "Route with path: {0} and type: {1} has already been\
               registered.".format(http_request.path, http_request.type)
        super().__init__(msg)