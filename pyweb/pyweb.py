from pyserver import WSGIPyServer
from pyweb.core.scheme import Scheme
from pyweb.endpoint import Endpoint
from pyweb.http.request import HttpRequest

class Pyweb:

    def __init__(self):
        self.scheme = Scheme()

    def route(self, path, type):
        def decorator(request_handler):
            endpoint = Endpoint(path, type, request_handler)
            self.scheme.register_endpoint(endpoint)
            return request_handler
        return decorator

    def wsgi_app(self, environ, start_response):
        status, headers, body = self.__get_app_response(environ)
        start_response(status, headers)
        return body

    def __get_app_response(self, environ):
        request = HttpRequest(environ)
        status, headers, body = self.scheme.process_request(request)
        return (status, headers, body)

    def run(self, debug=False):
        server = WSGIPyServer(self.wsgi_app)
        server.run()

