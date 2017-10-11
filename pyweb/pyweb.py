from pyserver import WSGIPyServer

class Pyweb:

    def wsgi_app(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)
        return ['Simple response']

    def run(self, debug=False):
        print('Run application...')
        server = WSGIPyServer(self.wsgi_app)
        server.run()


    def route(self, path, type):
        def decorator(f):
            return f
        return decorator
