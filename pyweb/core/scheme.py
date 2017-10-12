from pyweb.core.exceptions import EndpointAlreadyRegistered

class Scheme:

    def __init__(self):
        self.routes = dict()

    def register_endpoint(self, http_request):
        self.__check_is_url_registered(http_request)
        self.__add_endpoint_handler(http_request)

    def __check_is_url_registered(self, http_request):
        for route in self.routes:
            self.__check_if_handler_match(http_request, route)

    def __check_if_handler_match(self, http_request, route):
        if self.__check_if_paths_match(http_request, route):
            if self.__check_if_request_type_match(http_request, route):
                raise EndpointAlreadyRegistered(http_request)

    def __check_if_paths_match(self, http_request, route):
        request_path = http_request.path.split('/')
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
        return is_request_subpath_param == is_route_subpath_param

    def __is_url_param(self, subpath):
        return subpath.startswith('<') and subpath.endswith('>')

    def __check_if_request_type_match(self, http_request, route):
        return http_request.type in self.routes[route]

    def __add_endpoint_handler(self, http_request):
        path, type, request_handler = http_request.info()
        if not path in self.routes:
            self.routes[path] = {}
        self.routes[path][type] = request_handler