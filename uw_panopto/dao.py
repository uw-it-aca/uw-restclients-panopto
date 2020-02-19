import logging
import os
from os.path import abspath, dirname
from restclients_core.dao import DAO


class Panopto_DAO(DAO):
    def service_name(self):
        return 'panopto'

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]

    def is_using_file_dao(self):
        return self.get_implementation().is_mock()

    def _custom_headers(self, method, url, headers, body):
        custom_headers = {}

        token = self.get_service_setting('AUTH_TOKEN')
        if token is not None:
            custom_headers["Authorization"] = "Token {}".format(token)

        return custom_headers
