from uw_panopto import panopto_url, get_resource
from uw_panopto.models import RemoteRecorder
import json


def get_remote_recorders(query):
    """
    Return a restclients.models.panopto.RemoteRecorder object
    """

    url = "{}?searchQuery={}".format(
        panopto_url("remoteRecorders/search"), query)

    response = json.loads(get_resource(url))

    recorders = []
    for result in response["Results"]:
        recorders.append(RemoteRecorder(data=result))

    return recorders
