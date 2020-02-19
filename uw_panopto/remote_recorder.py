from uw_panopto import panopto_url
from uw_panopto.models import RemoteRecorder, RecordingFolder
from uw_panopto.util import get_paged_resource


def remote_recorder_search(query):
    """
    Search for remote recorders based on a keyword

    To fetch all elements, this endpoint can be called multiple times,
    starting at pageNumber = 0 and incrementing the page number until
    no results are returned.
    """

    url = "{}?searchQuery={}".format(
        panopto_url("remoteRecorders/search"), query)

    return get_paged_resource(url, recorder_from_json)


def recorder_from_json(recorder_data):
    recorder = RemoteRecorder(data=recorder_data)
    recorder.default_recording_folder = RecordingFolder(
        data=recorder_data["DefaultRecordingFolder"])
    return recorder
