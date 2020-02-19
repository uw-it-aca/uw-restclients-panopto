"""
This is the interface for interacting with
the Panopto REST API.
"""

import logging
from uw_panopto.dao import Panopto_DAO
from restclients_core.exceptions import DataFailureException


logger = logging.getLogger(__name__)


def panopto_url(api_path):
    return "/Panopto/api/v1/{}".format(api_path)


def get_resource(url):
    response = Panopto_DAO().getURL(url, {'Accept': 'application/json'})

    logger.debug("{0} ==status==> {1}".format(url, response.status))
    if response.status != 200:
        raise DataFailureException(url, response.status, response.data)

    logger.debug("{0} ==data==> {1}".format(url, response.data))
    return response.data
