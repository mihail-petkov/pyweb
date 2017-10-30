class HttpStatus:

    DEFAULT = 200
    NOT_FOUND = 404

    CODES = {}
    CODES[100] = "Continue"
    CODES[101] = "Switching Protocols"
    CODES[102] = "Processing"
    CODES[200] = "OK"
    CODES[201] = "Created"
    CODES[202] = "Accepted"
    CODES[203] = "Non-Authoritative Information"
    CODES[204] = "No Content"
    CODES[205] = "Reset Content"
    CODES[206] = "Partial Content"
    CODES[207] = "Multi-Status"
    CODES[208] = "Already Reported"
    CODES[226] = "IM Used"
    CODES[300] = "Multiple Choices"
    CODES[301] = "Moved Permanently"
    CODES[302] = "Found"
    CODES[303] = "See Other"
    CODES[304] = "Not Modified"
    CODES[305] = "Use Proxy"
    CODES[306] = "Switch Proxy"
    CODES[307] = "Temporary Redirect"
    CODES[308] = "Permanent Redirect"
    CODES[400] = "Bad Request"
    CODES[401] = "Unauthorized"
    CODES[402] = "Payment Required"
    CODES[403] = "Forbidden"
    CODES[404] = "Not Found"
    CODES[405] = "Method Not Allowed"
    CODES[406] = "Not Acceptable"
    CODES[407] = "Proxy Authentication Required"
    CODES[408] = "Request Timeout"
    CODES[409] = "Conflict"
    CODES[410] = "Gone"
    CODES[411] = "Length Required"
    CODES[412] = "Precondition Failed"
    CODES[413] = "Payload Too Large"
    CODES[414] = "URI Too Long"
    CODES[415] = "Unsupported Media Type"
    CODES[416] = "Range Not Satisfiable"
    CODES[417] = "Expectation Failed"
    CODES[418] = "I'm a teapot"
    CODES[421] = "Misdirected Request"
    CODES[422] = "Unprocessable Entity"
    CODES[423] = "Locked"
    CODES[424] = "Failed Dependency"
    CODES[426] = "Upgrade Required"
    CODES[428] = "Precondition Required"
    CODES[429] = "Too Many Requests"
    CODES[431] = "Request Header Fields Too Large"
    CODES[451] = "Unavailable For Legal Reasons"
    CODES[500] = "Internal Server Error"
    CODES[501] = "Not Implemented"
    CODES[502] = "Bad Gateway"
    CODES[503] = "Service Unavailable"
    CODES[504] = "Gateway Timeout"
    CODES[505] = "HTTP Version Not Supported"
    CODES[506] = "Variant Also Negotiates"
    CODES[507] = "Insufficient Storage"
    CODES[508] = "Loop Detected"
    CODES[510] = "Not Extended"
    CODES[511] = "Network Authentication Required"

    @classmethod
    def get(cls, status):
        return '{} {}'.format(status, cls.get_code_per_status(status))

    @classmethod
    def get_code_per_status(cls, status):
        if status in cls.CODES:
            return cls.CODES[status]
        return ''
