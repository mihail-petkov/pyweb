from pyweb.core.exceptions import EndpointAlreadyRegistered
from pyweb.logger.logger import logger

class Scheme:

    def __init__(self):
        self.routes = dict()

    def register_endpoint(self, endpoint):
        self.__check_is_url_registered(endpoint)
        self.__add_endpoint_handler(endpoint)

    def __check_is_url_registered(self, endpoint):
        handler = self.__find_request_handler(endpoint)
        if handler:
            raise EndpointAlreadyRegistered(endpoint)

    def __find_request_handler(self, endpoint):
        for route in self.routes:
            if self.__do_endpoint_exist(endpoint, route):
                return self.routes[route][endpoint.type]
        return None

    def __do_endpoint_exist(self, endpoint, route):
        if self.__check_if_paths_match(endpoint, route):
            if self.__check_if_request_type_match(endpoint, route):
                return True
        return False

    def __check_if_paths_match(self, endpoint, route):
        request_path = endpoint.path.split('/')
        route_path = route.split('/')
        if self.__subpaths_have_same_length(request_path, route_path):
            return self.__validate_every_subpath(request_path, route_path)
        return False

    def __subpaths_have_same_length(self, request_path, route_path):
        return len(request_path) == len(route_path)

    def __validate_every_subpath(self, request_path, route_path):
        for i, _ in enumerate(route_path):
            if self.__do_subpaths_type_match(request_path[i], route_path[i]):
                continue
            return False
        return True
    
    def __do_subpaths_type_match(self, request_subpath, route_subpath):
        is_request_subpath_param = self.__is_url_param(request_subpath)
        is_route_subpath_param = self.__is_url_param(route_subpath)
        if is_request_subpath_param == is_route_subpath_param:
            if is_request_subpath_param:
                return True
            else:
                return request_subpath == route_subpath
        return False

    def __is_url_param(self, subpath):
        return subpath.startswith('<') and subpath.endswith('>')

    def __check_if_request_type_match(self, endpoint, route):
        return endpoint.type in self.routes[route]

    def __add_endpoint_handler(self, endpoint):
        path, type, request_handler = endpoint.info()
        if not path in self.routes:
            self.routes[path] = {}
        self.routes[path][type] = request_handler

    def process_request(self, current_request):
        logger.info('Processing request {}'.format(current_request))
        request_handler = self.__find_request_handler(current_request)
        if not request_handler:
            return self.__not_found_response()
        app_response = request_handler()
        return ('200 OK', [('Content-Type', 'application/json')], str(app_response))

    def __not_found_response(self):
        return ('404 Not Found', [('Content-Type', 'text/plain')], str('Not found endpoint'))