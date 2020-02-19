from uw_panopto import (
    panopto_url, get_resource, put_resource, delete_resource, post_resource)
from uw_panopto.models import ScheduledRecording, RecorderScheduledEntry
import json


def get_scheduled_recordings(id):
    """
    Return a restclients.models.panopto.scheduledRecordings object
    """

    url = "{}/{}".format(
        panopto_url("scheduledRecordings"), id)

    response = json.loads(get_resource(url))
    return _scheduled_recordings(response)


def update_scheduled_recording_times(id, start_time=None, end_time=None):
    """
    Update the start or end time of a scheduled recording
    """

    if not start_time or end_time:
        return

    url = "{}/{}".format(
        panopto_url("scheduledRecordings"), id)

    times = {}

    if start_time:
        times["StartTime"] = str(start_time)

    if end_time:
        times["EndTime"] = str(end_time)

    response = put_resource(url, times)

    return _scheduled_recordings(response)


def delete_scheduled_recording(id):
    """
    Delete a scheduled recording
    """

    url = "{}/{}".format(
        panopto_url("scheduledRecordings"), id)

    delete_resource(url)


def create_scheduled_recording(name=None, description=None,
                               start_time=None, end_time=None,
                               folder_id=None, recorders=None,
                               is_broadcast=None):
    """
    Create a new scheduled recording
    """
    if (name is None or description is None or start_time is None or
            end_time is None or folder_id is None or
            not isinstance(recorders, list) or len(recorders) == 0 or
            not isinstance(is_broadcast, bool)):
        raise Exception("Incomplete Recording Schedule")

    url = panopto_url("scheduledRecordings")

    recording = {
        "Name": name,
        "Description": description,
        "StartTime": str(start_time),
        "EndTime": str(end_time),
        "FolderId": folder_id,
        "Recorders": [],
        "IsBroadcast": is_broadcast
    }

    for recorder in recorders:
        recording["Recorders"].append({
            "RemoteRecorderId": recorder.get('remote_recorder_id'),
            "SuppressPrimary": recorder.get('suppress_primary'),
            "SuppressSecondary": recorder.get('suppress_secondary')
        })

    response = post_resource(url, recording)

    return _scheduled_recordings(response)


def _scheduled_recordings(response):
    scheduled_recordings = ScheduledRecording(data=response)
    scheduled_recordings.recorder_schedule_entries = []

    for rse in response['RecorderScheduleEntries']:
        scheduled_recordings.recorder_schedule_entries.append(
            RecorderScheduledEntry(data=rse))

    return scheduled_recordings
