from pyweb.exceptions.base import PyWebException

class NotAllowedRequestTypeException(PyWebException):

    def __init__(self, type):
        super().__init__("Request type {0} is not allowed.".format(type))