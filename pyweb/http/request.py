from pyweb.http.request_type import HttpRequestType
from pyweb.http.exception import NotAllowedRequestTypeException

class HttpRequest:

    def __init__(self, path, type, handler):
        self.path = path
        self.type = type
        self.handler = handler
        self.__validate_request_details()
        self.__format_path()

    def info(self):
        return (self.path, self.type, self.handler)

    def __validate_request_details(self):
        self.__validate_type()

    def __validate_type(self):
        if not self.type in HttpRequestType.ALLOWED_REQUEST_TYPES:
            raise NotAllowedRequestTypeException(self.type)

    def __format_path(self):
        self.__convert_slashes_to_backslashes()
        self.__remove_last_slash()
        self.__remove_double_slashes()

    def __convert_slashes_to_backslashes(self):
        # TODO: 
        print('converting...')

    def __remove_last_slash(self):
        if self.path.endswith('/'):
            self.path = self.path[:-1]

    def __remove_double_slashes(self):
        self.path = self.path.replace('//', '/')
