from restclients_core.util.decorators import use_mock
from uw_panopto import get_resource
from uw_panopto.dao import Panopto_DAO
import json

fdao_panopto_override = use_mock(Panopto_DAO())


def get_paged_resource(url, processor):
    """
    """

    resources = []
    page = 0
    delim = '&' if '?' in url else '?'
    while True:
        paged_url = "{}{}pageNumber={}".format(url, delim, page)
        response = json.loads(get_resource(paged_url))

        if "Results" not in response or len(response["Results"]) == 0:
            break
        else:
            page += 1

        for paged_data in response["Results"]:
            resources.append(processor(paged_data))

    return resources
