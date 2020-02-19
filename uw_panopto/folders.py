from uw_panopto import (
    panopto_url, get_resource, put_resource, delete_resource)
from uw_panopto.models import Folder, FolderUrls, RecordingFolder
from uw_panopto.util import get_paged_resource
from uw_panopto.sessions import session_from_json
import json


def get_folder(id):
    """
    Get a folder by id
    """
    url = "{}/{}".format(
        panopto_url("folders"), id)

    response = json.loads(get_resource(url))
    return folder_from_json(response)


def folder_search(query):
    """
    Search for folders based on a keyword

    To fetch all elements, this endpoint can be called multiple times,
    starting at pageNumber = 0 and incrementing the page number until
    no results are returned.
    """
    url = "{}?searchQuery={}".format(
        panopto_url("folders/search"), query)

    return get_paged_resource(url, folder_from_json)


def get_folder_children(id):
    """
    Get a list of child folders from the given parent

    To fetch all elements, this endpoint can be called multiple times,
    starting at pageNumber = 0 and incrementing the page number until
    no results are returned.
    """
    url = "{}/{}/children".format(panopto_url("folders"), id)

    return get_paged_resource(url, folder_from_json)


def get_folder_sessions(id):
    """
    Get a list of sessions in the given folder

    To fetch all elements, this endpoint can be called multiple times,
    starting at pageNumber = 0 and incrementing the page number until
    no results are returned.
    """
    url = "{}/{}/sessions".format(panopto_url("folders"), id)

    return get_paged_resource(url, session_from_json)


def update_folder(id, name=None, description=None, parent=None):
    """
    Update the folders's name, description, or parent folder.
    """
    url = "{}/{}".format(panopto_url("folders"), id)

    if not name and not description and not parent:
        raise Exception("Incomplete folder update")

    folder = {}

    if name:
        folder["Name"] = name

    if description:
        folder["Description"] = description

    if folder:
        folder["Parent"] = parent

    response = put_resource(url, folder)
    return folder_from_json(response)


def delete_folder(id):
    """
    Deletes a folder and all of its contents (including sessions
    and subfolders) according to the retention policy.
    """
    url = "{}/{}".format(panopto_url("folders"), id)

    delete_resource(url)


def folder_from_json(folder_data):
    folder = Folder(data=folder_data)
    folder.parent_folder = RecordingFolder(
        data=folder_data.get("ParentFolder"))
    folder.urls = FolderUrls(data=folder_data.get("Urls"))
    return folder
