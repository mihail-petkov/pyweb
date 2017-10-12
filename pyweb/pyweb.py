from pyserver import WSGIPyServer
from pyweb.core.scheme import Scheme
from pyweb.http.request import HttpRequest

class Pyweb:

    def __init__(self):
        self.scheme = Scheme()

    def route(self, path, type):
        def decorator(request_handler):
            request = HttpRequest(path, type, request_handler)
            self.scheme.register_endpoint(request)
            return request_handler
        return decorator

    def wsgi_app(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)
        return ['Simple response']

    def run(self, debug=False):
        print('Run application...')
        server = WSGIPyServer(self.wsgi_app)
        server.run()
