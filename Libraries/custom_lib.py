import requests
from urllib.parse import urljoin


class custom_lib(object):

    def __init__(self):
        self._result = ''

    # Basic auth for httpbin.org
    def custom_basic_auth(self, url, user, password):
        self._result = requests.get(url, auth=(user, password))
        return self._result.status_code

    # Get request for httpbin.org
    def custom_get(self, url):
        self._result = requests.get(url)

    # Stream request for httpbin.org
    def custom_stream(self, url, n):
        self._result = requests.get(url.strip('/') + '/' + str(n))

    # Authentication check for the result
    def get_authenticated(self):
        return self._result.json()['authenticated']

    # Get headers from the get response (not the request headers)
    def get_headers(self):
        return self._result.json()['headers']

    # Get number of lines in the response
    def get_lines(self):
        return len(list(self._result.iter_lines()))

    # Get status code from the response
    def get_status(self):
        return self._result.status_code
