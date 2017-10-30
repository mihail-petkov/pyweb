from pyweb.core.exceptions import EndpointAlreadyRegistered
from pyweb.logger.logger import logger
from pyweb.http.status import HttpStatus
from pyweb.http.response import HttpResponse
import pyweb.ctx as ctx

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
        request_url = endpoint.path.split('?')[0]
        request_path = request_url.split('/')
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
        is_route_subpath_param = self.__is_url_param(route_subpath)
        if is_route_subpath_param:
            return True
        else:
            return request_subpath == route_subpath

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
        ctx.request = current_request
        logger.info('Processing request {}'.format(current_request))
        request_handler = self.__find_request_handler(current_request)
        if not request_handler:
            logger.info('Request handler does not exist')
            return self.__not_found_response()
        request_params = self.__get_request_path_params(current_request)
        app_response = request_handler(*request_params)
        return self.__return_to_server(app_response)

    def __get_request_path_params(self, request):
        origin_route = self.__find_route_description(request).split('/')
        route_parts = request.path.split('/')
        return self.__get_path_params(origin_route, route_parts)

    def __find_route_description(self, request):
        for route in self.routes:
            if self.__do_endpoint_exist(request, route):
                return route

    def __get_path_params(self, origin_route, route_parts):
        params = []
        for i, _ in enumerate(origin_route):
            if self.__is_url_param(origin_route[i]):
                params.append(route_parts[i])
        return params

    def __not_found_response(self):
        response = '', HttpStatus.NOT_FOUND
        return self.__return_to_server(response)

    def __return_to_server(self, raw_response):
        response = HttpResponse(raw_response)
        status = response.get_formatted_status()
        headers = response.get_headers()
        body = response.get_body()
        return (status, headers, body)