"""Flask Logging

Usage:

from flask.ext.logging import Filter
filter = Filter('static')

Filters any request with the word 'static' from the log.

Filtering more than one word:

filter = Filter('static', 'admin')
"""


class Filter(object):
    def __init__(self, *filters):
        from werkzeug import serving

        _log_request = serving.WSGIRequestHandler.log_request

        def log_request(self, *args, **kwargs):
            if any(filter in self.requestline for filter in filters):
                return

            _log_request(self, *args, **kwargs)

        serving.WSGIRequestHandler.log_request = log_request
