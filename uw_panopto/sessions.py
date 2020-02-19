from uw_panopto import (
    panopto_url, get_resource, put_resource, delete_resource, post_resource)
from uw_panopto.models import (
    Session, SessionCreator, SessionUrls, SessionContext)
import json


def get_session(id):
    """
    Return a restclients.models.Session object
    """
    url = "{}/{}".format(panopto_url("sessions"), id)

    response = json.loads(get_resource(url))
    return _session(response)


def _session(response):
    session = Session(data=response)
    session.created_by = SessionCreator(data=response.get("CreatedBy"))
    session.urls = SessionUrls(data=response.get("Urls"))
    session.context = []
    for c in response.get("Context"):
        session.context.append(SessionContext(data=c))

    return session
