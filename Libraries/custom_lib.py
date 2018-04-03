# 5. Используя эту библиотеку, написать автотесты на Robot Framework,
# реализующие как минимум:
# a. Проверку аутентификации при различных user, password
# (используя data driven подход, реализуемый при помощи Template)
# b. Проверку какого-либо header в возвращаемом ответе /get
# c. Проверку количества строк в возвращаемом запросе /stream
# d. Проверка кода возврата во всех ответах
# 6. Все проверки должны быть в коде автотестов, а не в библиотеке

import requests
from urllib.parse import urljoin


class custom_lib(object):

    def __init__(self):
        self._result = ''

    def custom_basic_auth(self, url, user, password):
        self._result = requests.get(url, auth=(user, password))
        return self._result.status_code

    def custom_get(self, url):
        self._result = requests.get(url)

    def custom_stream(self, url, n):
        self._result = requests.get(url.strip('/') + '/' + str(n))

    # a. Проверку аутентификации при различных user, password
    # (используя data driven подход, реализуемый при помощи
    # Template)
    def check_authenticated(self, b):
        try:
            auth = self._result.json()['authenticated']
            if auth != b:
                raise AssertionError(("Authentication error:"
                                      "Authenticated: %s, "
                                      "Expected %s") % (auth, b))
        except:
            raise AssertionError(self._result.content)

    # b. Проверку какого-либо header в возвращаемом ответе /get
    def get_headers(self):
        return self._result.json()['headers']
        # if received != string:
        #     raise AssertionError(("Wrong header %s:"
        #                           "Received %s, "
        #                           "Expected %s") % (key, received, expected))

    # c. Проверку количества строк в возвращаемом запросе /stream
    def check_lines(self, n):
        l = len(list(self._result.iter_lines()))
        if l != n:
            raise AssertionError(("Wrong number of lines:"
                                  "Received %d, "
                                  "Expected %d") % (l, n))

    # d. Проверка кода возврата во всех ответах
    def check_status(self, n):
        if self._result.status_code != n:
            raise AssertionError(("Wrong status code:"
                                  " %d, Expected %d") %
                                 (self._result.status_code, n))

