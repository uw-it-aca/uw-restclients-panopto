from os.path import abspath, dirname
from restclients_core.dao import DAO
from restclients_core.exceptions import DataFailureException
import json
import os


class Panopto_DAO(DAO):
    def __init__(self, *args, **kwargs):
        super(Panopto_DAO, self).__init__(*args, **kwargs)

        url = "{}/Panopto/oauth2/connect/token".format(
            self.get_service_setting('HOST'))

        auth = "Basic {}".format(
            self.get_service_setting('AUTH_TOKEN'))

        response = self.postURL(url, {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': auth
        }, "grant_type=client_credentials&scope=api")

        if response.status == 200:
            self.access_token = json.loads(response.data)["access_token"]
        else:
            raise DataFailureException(
                url, response.status,
                json.loads(response.data)["error"] if (
                    response.status == 400) else "Cannot get access token")

    def service_name(self):
        return 'panopto'

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]

    def is_using_file_dao(self):
        return self.get_implementation().is_mock()

    def _custom_headers(self, method, url, headers, body):
        return {
            "Authorization": "Bearer {}".format(self.access_token)
        } if hasattr(self, 'access_token') else {}
