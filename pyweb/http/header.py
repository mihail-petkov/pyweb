class HttpHeader:

    DEFAULT = {}
    DEFAULT['Content-Type'] = 'application/json'

    @classmethod
    def merge_default_headers(cls, request_headers):
        for header in cls.DEFAULT:
            if not header in request_headers:
                request_headers[header] = cls.DEFAULT[header]
        return request_headers
