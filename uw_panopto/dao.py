from os.path import abspath, dirname
from restclients_core.dao import DAO
from restclients_core.exceptions import DataFailureException
from datetime import datetime
import json
import os


panopto_dao_access_token = None


class Panopto_DAO(DAO):
    def __init__(self, *args, **kwargs):
        super(Panopto_DAO, self).__init__(*args, **kwargs)

        global panopto_dao_access_token

        if self.get_implementation().is_mock():
            return

        if (not panopto_dao_access_token or
            ((datetime.utcnow() -
              panopto_dao_access_token["fetched"]).seconds) >=
                panopto_dao_access_token["expires_in"]):
            url = "{}/Panopto/oauth2/connect/token".format(
                self.get_service_setting('HOST'))

            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': "Basic {}".format(
                    self.get_service_setting('AUTH_TOKEN'))
            }

            body = "grant_type=client_credentials&scope=api"

            response = self.postURL(url, headers, body)

            if response.status == 200:
                panopto_dao_access_token = json.loads(response.data)
                panopto_dao_access_token["fetched"] = datetime.utcnow()
            else:
                raise DataFailureException(
                    url, response.status,
                    json.loads(response.data)["error"] if (
                        response.status == 400) else "Cannot get access token")

        self.access_token = panopto_dao_access_token

    def service_name(self):
        return 'panopto'

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]

    def is_using_file_dao(self):
        return self.get_implementation().is_mock()

    def _custom_headers(self, method, url, headers, body):
        return {
            "Authorization": "{} {}".format(
                self.access_token["token_type"],
                self.access_token["access_token"])
        } if hasattr(self, 'access_token') else {}
