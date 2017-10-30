from pyweb.http.status import HttpStatus
from pyweb.http.header import HttpHeader
import json

class HttpResponse:

    def __init__(self, response):
        self.raw_response = response

    def get_formatted_status(self):
        status = self.get_status()
        return HttpStatus.get(status)

    def get_status(self):
        status = HttpStatus.DEFAULT
        if self.__has_custom_status():
            status = self.raw_response[1]
        return status

    def __has_custom_status(self):
        return len(self.raw_response) > 1

    def get_headers(self):
        response_headers = self.__get_response_headers()
        headers = HttpHeader.merge_default_headers(response_headers)
        return self.__format_headers(headers)

    def __get_response_headers(self):
        if self.__has_custom_headers():
            return self.raw_response[2]
        return {}

    def __has_custom_headers(self):
        return len(self.raw_response) > 2

    def __format_headers(self, headers):
        return [(key, headers[key]) for key in headers]


    def get_body(self):
        if self.__has_custom_status():
            return json.dumps(self.raw_response[0])
        return json.dumps(self.raw_response)