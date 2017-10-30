class HttpRequest:

    def __init__(self, environ):
        self.type = environ['REQUEST_METHOD']
        self.path = environ['PATH_INFO']
        self.body = self.__parse_body(environ)
        self.params = {}
        self.__set_path_variables()

    def __parse_body(self, environ):
        return environ['wsgi.input'].read().split('\\r\\n')[-1][:-1]

    def __set_path_variables(self):
        splitted_url = self.path.split('?')
        if self.__has_path_variables(splitted_url):
            self.__parse_path(splitted_url[1])

    def __has_path_variables(self, splitted_url):
        return len(splitted_url) > 1

    def __parse_path(self, path):
        params = path.split('&')
        for key in params:
            current_param = key.split('=')
            self.params[current_param[0]] = current_param[1]