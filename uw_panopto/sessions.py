from uw_panopto import (
    panopto_url, get_resource, put_resource, delete_resource, post_resource)
from uw_panopto.models import (
    Session, SessionCreator, SessionUrls, SessionContext)
from uw_panopto.util import get_paged_resource
import json


def get_session(id):
    """
    Get a session by Id
    """
    url = "{}/{}".format(panopto_url("sessions"), id)

    response = json.loads(get_resource(url))
    return session_from_json(response)


def session_search(query):
    """
    Search for sessions based on a keyword

    To fetch all elements, this endpoint can be called multiple times,
    starting at pageNumber = 0 and incrementing the page number until
    no results are returned.

    Note: The Session Search API does not return all available properties
    for a session. The CreatedBy and Urls properties (except the ViewerUrl
    and ThumbnailUrl) are not returned when searching for a session.
    To get these properties, you can get the specific session by Id.
    """

    url = "{}?searchQuery={}".format(
        panopto_url("sessions/search"), query)

    return get_paged_resource(url, session_from_json)


def update_session(id, name=None, description=None, folder=None):
    """
    Update the session's name, description, or parent folder
    """
    url = "{}/{}".format(panopto_url("sessions"), id)

    if not name and not description and not folder:
        raise Exception("Incomplete recording schedule update")

    session = {}

    if name:
        session["Name"] = name

    if description:
        session["Description"] = description

    if folder:
        session["Folder"] = folder

    response = put_resource(url, session)
    return session_from_json(response)


def delete_session(id):
    """
    Deletes a session based on the retention policies
    """
    url = "{}/{}".format(panopto_url("sessions"), id)

    delete_resource(url)


def session_from_json(session_data):
    session = Session(data=session_data)
    session.created_by = SessionCreator(data=session_data.get("CreatedBy"))
    session.urls = SessionUrls(data=session_data.get("Urls"))
    session.context = []
    for c in session_data.get("Context"):
        session.context.append(SessionContext(data=c))

    return session
