from uw_panopto import panopto_url, get_resource
from uw_panopto.models import ScheduledRecording, RecorderScheduledEntry
import json


def get_scheduled_recordings(id):
    """
    Return a restclients.models.panopto.scheduledRecordings object
    """

    url = "{}/{}".format(
        panopto_url("scheduledRecordings"), id)

    response = json.loads(get_resource(url))
    scheduled_recordings = ScheduledRecording(data=response)
    scheduled_recordings.recorder_schedule_entries = []

    for rse in response['RecorderScheduleEntries']:
        scheduled_recordings.recorder_schedule_entries.append(
            RecorderScheduledEntry(data=rse))

    return scheduled_recordings
