class HttpRequest:

    def __init__(self, environ):
        self.type = environ['REQUEST_METHOD']
        self.path = environ['PATH_INFO']
        self.body = self.__parse_body(environ)

    def __parse_body(self, environ):
        return environ['wsgi.input'].read().split('\\r\\n')[-1][:-1]