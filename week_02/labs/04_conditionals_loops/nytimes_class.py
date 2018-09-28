import json
import sys

class MyApp:

    def dispatch(self, environ):
        query = environ['QUERY_STRING']
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']

        if method == 'GET':
            # do something
            return "temp"
        return "Your request is invalid, please try new URL"
