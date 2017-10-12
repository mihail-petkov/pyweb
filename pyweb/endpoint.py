from pyweb.http.request_type import HttpRequestType

class Endpoint:
    def __init__(self, path, type, handler):
        self.__path = path
        self.__type = type
        self.__handler = handler
        self.__validate_request_details()
        self.__format_path()

    def info(self):
        return (self.__path, self.__type, self.__handler)

    def __validate_request_details(self):
        self.__validate_type()

    def __validate_type(self):
        if not self.__type in HttpRequestType.ALLOWED_REQUEST_TYPES:
            raise NotAllowedRequestTypeException(self.__type)

    def __format_path(self):
        self.__convert_slashes_to_backslashes()
        self.__remove_last_slash()
        self.__remove_double_slashes()

    def __convert_slashes_to_backslashes(self):
        # TODO: 
        print('converting...')

    def __remove_last_slash(self):
        if self.__path.endswith('/'):
            self.__path = self.__path[:-1]

    def __remove_double_slashes(self):
        self.__path = self.path.replace('//', '/')

    @property
    def path(self):
        return self.__path

    @property
    def type(self):
        return self.__type